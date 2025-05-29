import sys
input = sys.stdin.readline

class Stack:

    def __init__(self,capacity):
        self.capacity = capacity
        self.top = -1
        self.stk = [None] * capacity

    def __len__(self):
        return self.top + 1
    
    def is_empty(self):
        if self.top == -1:
            return 1
        else:
            return 0
    
    def is_full(self):
        if self.top == self.capacity - 1:
            return 1
        else:
            return 0
    
    def push(self,value):
        if self.is_full():
            return -1
        self.top += 1
        self.stk[self.top] = value
    
    def peek(self):
        if self.is_empty():
            return -1
        return self.stk[self.top]

    def pop(self):
        if self.is_empty():
            return -1
        item = self.stk[self.top]
        self.top -= 1
        return item
    
    def clear(self):
        self.top = -1

st = Stack(10000)
n = int(input())

for _ in range(n):
    cmd = input()
    cmd = cmd.strip()
    if 'push' in cmd:
        cmd,value = cmd.split()
        value = int(value)
        st.push(value)
    elif cmd == 'pop':
        print(st.pop())
    elif cmd == 'top':
        print(st.peek())
    elif cmd == 'size':
        print(st.__len__())
    else:
        print(st.is_empty())


        

