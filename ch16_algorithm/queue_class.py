# queue_class.py


class Queue:
    def __init__(self):
        self.queue = []

    # 1. Enqueue
    def enqueue(self, data):
        self.queue.append(data)

    # 2. Dequeue
    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        return 

    # 3. 큐가 비어있는 경우
    def is_empty(self):
        if len(self.queue) == 0:
            return True
        return False

    # 4. 큐 상태 반환
    def status_queue(self):
        return self.queue

if __name__ == "__main__":
    q1 = Queue()
    q1.dequeue()
    q1.enqueue(1)
    print(f"queue = {q1.status_queue()}")
    q1.enqueue(2)
    print(f"queue = {q1.status_queue()}")
    q1.dequeue()
    q1.enqueue(3)
    print(f"queue = {q1.status_queue()}")
    q1.enqueue(4)
    print(f"queue = {q1.status_queue()}")
    q1.dequeue()
    print(f"queue = {q1.status_queue()}")

