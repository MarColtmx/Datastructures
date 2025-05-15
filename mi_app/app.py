from flask import Flask, render_template, request, redirect, flash, session, url_for
import sqlite3
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'clave_secreta'

# Conexión a la base de datos
def get_db_connection():
    conn = sqlite3.connect('ventas.db')
    conn.row_factory = sqlite3.Row
    return conn

# Inicializa la BD con algunos productos si está vacía
def inicializar_bd():
    conn = get_db_connection()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS productos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            precio REAL NOT NULL,
            stock INTEGER NOT NULL
        )
    ''')
    productos = conn.execute("SELECT * FROM productos").fetchall()
    if not productos:
        conn.executemany("""
            INSERT INTO productos (nombre, precio, stock) VALUES (?, ?, ?)
        """, [
            ("Mouse", 15.0, 50),
            ("Teclado", 30.0, 20),
            ("Monitor", 100.0, 10)
        ])
    conn.commit()
    conn.close()

@app.route('/', methods=['GET', 'POST'])
def index():
    if 'productos_vendidos' not in session:
        session['productos_vendidos'] = []

    productos_vendidos = session['productos_vendidos']

    if request.method == 'POST':
        codigo_producto = request.form['codigo_producto']

        conn = get_db_connection()
        producto = conn.execute(
            "SELECT * FROM productos WHERE id = ? OR nombre LIKE ?",
            (codigo_producto, f"%{codigo_producto}%")
        ).fetchone()
        conn.close()

        if producto:
            productos_vendidos.append({
                'id': producto['id'],
                'nombre': producto['nombre'],
                'precio': producto['precio']
            })
            session['productos_vendidos'] = productos_vendidos
            flash(f"Producto agregado: {producto['nombre']}")
        else:
            flash("Producto no encontrado")

    total_venta = sum(p['precio'] for p in productos_vendidos)

    return render_template(
        "index.html",
        productos_vendidos=productos_vendidos,
        total_venta=total_venta
    )

@app.route('/finalizar_venta', methods=['POST'])
def finalizar_venta():
    productos_vendidos = session.get('productos_vendidos', [])
    if not productos_vendidos:
        flash("No hay productos para vender.")
        return redirect(url_for('index'))

    total_venta = sum(p['precio'] for p in productos_vendidos)
    ticket_id = datetime.now().strftime("%Y%m%d%H%M%S")

    conn = get_db_connection()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS tickets (
            ticket_id TEXT PRIMARY KEY,
            productos TEXT,
            total REAL,
            fecha TEXT
        )
    """)
    conn.execute(
        "INSERT INTO tickets (ticket_id, productos, total, fecha) VALUES (?, ?, ?, ?)",
        (ticket_id, str(productos_vendidos), total_venta, datetime.now())
    )

    for producto in productos_vendidos:
        conn.execute(
            "UPDATE productos SET stock = stock - 1 WHERE id = ?",
            (producto['id'],)
        )

    conn.commit()
    conn.close()

    session['productos_vendidos'] = []
    flash(f"Venta finalizada. Ticket ID: {ticket_id}")
    return redirect(url_for('index'))

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    conn = get_db_connection()

    if request.method == 'POST':
        if 'agregar_producto' in request.form:
            nombre = request.form['nombre']
            precio = float(request.form['precio'])
            stock = int(request.form['stock'])
            conn.execute("INSERT INTO productos (nombre, precio, stock) VALUES (?, ?, ?)",
                         (nombre, precio, stock))
            flash(f"Producto '{nombre}' agregado exitosamente.")

        elif 'eliminar_producto' in request.form:
            producto_id = int(request.form['producto_id'])
            conn.execute("DELETE FROM productos WHERE id = ?", (producto_id,))
            flash("Producto eliminado exitosamente.")

        elif 'actualizar_stock' in request.form:
            producto_id = int(request.form['producto_id'])
            cantidad = int(request.form['cantidad'])
            conn.execute("UPDATE productos SET stock = stock + ? WHERE id = ?",
                         (cantidad, producto_id))
            flash("Stock actualizado exitosamente.")

        conn.commit()

    productos = conn.execute("SELECT * FROM productos").fetchall()
    conn.close()

    return render_template("admin.html", productos=productos)

if __name__ == '__main__':
    inicializar_bd()
    app.run(debug=True)
