from collections import deque

class Stack:

    def __init__(self,capacity):
        self.capacity = capacity
        self.__stk = deque([],capacity)

    def __len__(self):
        return len(self.__stk)
    
    def is_empty(self):
        return not self.__stk
    
    def is_full(self):
        return len(self.__stk) == self.__stk.maxlen
    
    def push(self,value):
        self.__stk.append(value)

    def pop(self):
        return self.__stk.pop()
    
    def clear(self):
        self.__stk.clear()

    def find(self,value):
        try:
            return self.__stk.index(value)
        except ValueError:
            return -1