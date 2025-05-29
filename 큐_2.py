import sys
input = sys.stdin.readline
class FixedQueue: 
    def __init__(self,capacity):
        self.no = 0
        self.front = 0
        self.rear = 0
        self.capacity = capacity
        self.que = [None] * capacity
    
    def is_empty(self):
        if self.front == self.rear:
            return 1
        return 0
    
    def is_full(self):
        return self.rear >= self.capacity
    
    def enque(self,item):
        if self.is_full():
            return -1
        self.no += 1
        self.que[self.rear] = item
        self.rear = (self.rear + 1) % self.capacity

    def deque(self):
        if self.is_empty() == 1:
            return -1
        self.no -= 1
        item = self.que[self.front]
        self.front = (self.front + 1) % self.capacity
        return item
    
    def peek(self):
        if self.is_empty() == 1:
            return -1
        return self.que[self.front]
    
    def count(self,value):
        cnt = 0
        for i in range(self.capacity):
            if self.que[i] == value:
                cnt+=1
        return cnt
    
    def size(self):
        return self.no
    
    def back(self):
        if self.is_empty() == 1:
            return -1
        return self.que[self.rear-1]
    

n = int(input())
q = FixedQueue(n)

for _ in range(n):
    cmd = input().strip()
    if 'push' in cmd:
        cmd,value = cmd.split()
        value = int(value)
    if cmd == 'push':
        q.enque(value)
    elif cmd == 'pop':
        print(q.deque())
    elif cmd == 'size':
        print(q.size())
    elif cmd == 'front':
        print(q.peek())
    elif cmd == 'back':
        print(q.back())
    else:
        print(q.is_empty())
