# Implement a Queue Data Structure
print("\nRuban Gino Singh - Day 99 of #100DaysOfCode\n")

print("Python program to Implement a Queue Data Structure.\n")

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
            raise IndexError("Queue is empty")

    def size(self):
        return len(self.items)

    def peek(self):
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError("Queue is empty")

if __name__ == "__main__":
    my_queue = Queue()

    my_queue.enqueue(1)
    my_queue.enqueue(2)
    my_queue.enqueue(3)

    print("Queue:", my_queue.items)

    removed_item = my_queue.dequeue()
    print("Dequeued item:", removed_item)
    print("Queue after dequeue:", my_queue.items)

    front_item = my_queue.peek()
    print("Front item:", front_item)

    print("Is the queue empty?", my_queue.is_empty())

# --------------------------------------------------------- #