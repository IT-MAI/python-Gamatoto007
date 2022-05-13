class Queue:
    def __init__(self):
        self.queue = []
    def enqueue(self, item):
        self.queue.append(item)
    def dequeue(self):
        if len(self.queue) >= 1:
            return self.queue.pop(0)
    def size(self):
        return len(self.queue)
    def isEmpty(self):
        if len(self.queue) > 0:
            return True
        else:
            return False
q=Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.dequeue()
q.size()
print(q.queue)
print(q.isEmpty())
print("Размер очереди: ", q.size())