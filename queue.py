class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        return self.queue.pop(0)

    def print_queue(self):
        print(f"ochered: {self.queue}")

    def peek(self):
        return print(self.queue[0])

# initializes queue attribute to an empty list
queue1 = Queue()
queue1.enqueue("hui")
queue1.enqueue("hii")
queue1.print_queue()
queue1.dequeue()
queue1.dequeue()
queue1.print_queue()










