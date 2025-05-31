class FixedQueue:
    class Empty(Exception):
        pass
    class Full(Exception):
        pass

    def __init__(self,capacity):
        self.front = 0
        self.rear = 0
        self.capacity = capacity
        self.que = [None] * capacity
    
    def is_empty(self):
        return self.front == self.rear
    
    def is_full(self):
        return self.rear >= self.capacity
    
    def enque(self,item):
        if self.is_full():
            raise FixedQueue.Full
        self.que[self.rear] = item
        self.rear = (self.rear + 1) % self.capacity

    def deque(self):
        if self.is_empty():
            raise FixedQueue.Empty
        item = self.que[self.front]
        self.front = (self.front + 1) % self.capacity
        return item
    
    def count(self,value):
        cnt = 0
        for i in range(self.capacity):
            if self.que[i] == value:
                cnt+=1
        return cnt
