import FIFO

q = FIFO.Queue()
q.enqueue('a')
q.enqueue(4)
q.enqueue(7)

print(q.dequeue())
print(q.dequeue())
print(q.dequeue())



