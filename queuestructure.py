from collections import deque

cola = deque()
cola.append("A")       # enqueue
cola.append("B")
print(cola.popleft())  # dequeue → A
print(cola[0])         # peek → B
