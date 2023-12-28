# Implement a Heap
print("\nRuban Gino Singh - Day 93 of #100DaysOfCode\n")

print("Python program to Implement a Heap.\n")

class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            print("Queue is empty")

    def front(self):
        if not self.is_empty():
            return self.items[0]
        else:
            print("Queue is empty")

    def size(self):
        return len(self.items)

queue = Queue()

print("Is the queue empty?", queue.is_empty())

queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print("Queue front:", queue.front())
print("Queue size:", queue.size())

dequeued_item = queue.dequeue()
print("Dequeued item:", dequeued_item)

print("Is the queue empty?", queue.is_empty())

# --------------------------------------------------------- #