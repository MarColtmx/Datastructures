import sqlite3

conn = sqlite3.connect("mi_base_de_datos.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Productos (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Nombre TEXT,
    Precio REAL,
    Stock INTEGER
)
""")
conn.commit()

# Insertar un producto usando parámetros (¡evita inyecciones SQL!)
cursor.execute("INSERT INTO productos (nombre, precio, stock) VALUES (?, ?, ?)", 
               ("Teclado", 29.99, 10))
conn.commit()

# Actualizar stock del producto con ID 1
cursor.execute("UPDATE productos SET stock = ? WHERE id = ?", (20, 1))
conn.commit()

# Obtener todos los productos
cursor.execute("SELECT * FROM productos")
productos = cursor.fetchall()

for producto in productos:
    print(producto)


# Eliminar el producto con ID 1
cursor.execute("DELETE FROM productos WHERE id = ?", (9,))
conn.commit()

conn.close()