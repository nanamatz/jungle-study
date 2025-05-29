class FixedStack:
    class Empty(Exception):
        pass
    class Full(Exception):
        pass

    def __init__(self,capacity):
        self.stk = [None] * capacity
        self.capacity = capacity
        self.ptr = 0

    def __len__(self):
        return self.ptr
    
    def is_empty(self):
        return self.ptr <= 0
    
    def is_full(self):
        return self.ptr >= self.capacity
    
    def push(self,value):
        if self.is_full():
            raise FixedStack.Full
        self.stk[self.ptr] = value
        self.ptr += 1
    
    def pop(self):
        if self.is_empty():
            raise FixedStack.Empty
        self.ptr -= 1
        return self.stk[self.ptr]
    
    def peek(self):
        if self.is_empty():
            raise FixedStack.Empty
        return self.stk[self.ptr - 1]

    def clear(self):
        self.ptr = 0

    def find(self,value):
        for i in range(self.ptr -1, -1, -1):    #ptr-1 부터 0까지 거꾸로 탐색
            if self.stk[i] == value:
                return i
        return -1
    
    def count(self,value):
        cnt = 0
        for i in range(self.ptr -1,-1,-1):
            if self.stk[i] == value:
                cnt += 1
        return cnt

    