import queue


class Coda_Prioritaria:

    def __init__(self):
        self._lista = []

    def put(self, valore):
        self._lista.append(valore)

    def pop(self):
        pos_min, val_min = min(enumerate(self._lista), key=lambda t: t[1])
        # enumerate trasforma la lista in una lista di tuple con indice e valore della lista originale
        # la lambda usa come chiave di comparazione il secondo elemento della tupla (il valore della lista)
        self._lista.pop(pos_min)  # il min restituisce una tupla e faccio il pop della posizione
        return val_min


c = Coda_Prioritaria()
c.put((2, "Paolo"))  # posso assegnare la priorità creando una tupla che esplicita direttamente la priorità!
c.put((1, "Giulia"))
c.put((2, "Antonio"))
c.put((1, "Anna"))
print(c.pop())
print(c.pop())
print(c.pop())

c1 = queue.PriorityQueue()
c1.put((2, "Paolo"))  # la classe apposta è più efficiente
c1.put((1, "Giulia"))
c1.put((2, "Antonio"))
c1.put((1, "Anna"))
print(c1.get())
print(c1.get())
print(c1.get())
# questo tipo di code vengono utilizzate nelle simulazioni di processi! (è una struttura di nicchia)
