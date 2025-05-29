import sys
input = sys.stdin.readline

n = int(input())

class Heap():
    def __init__(self,capacity):
        self.size = 0
        self.arr = [None] * (capacity + 1)
        self.capacity = capacity
    
    def insert(self,value):
        self.size += 1
        i = self.size

        while(i != 1 and value > self.arr[i//2]):
            self.arr[i] = self.arr[i//2]
            i = i//2
        self.arr[i] = value

    def delete(self):
        if self.size == 0 :
            return 0
        
        item = self.arr[1]
        temp = self.arr[self.size]

        self.size -= 1
        
        parent = 1
        child = 2

        while(child <= self.size):

            if child < self.size and self.arr[child] < self.arr[child+1]:
                child += 1
            
            if temp >= self.arr[child]:
                break
            
            self.arr[parent] = self.arr[child]
            parent = child
            child *= 2

        self.arr[parent] = temp

        return item

h = Heap(n)

# print(h.size())
for _ in range(n):
    cmd = int(input())
    if cmd == 0:
        print(h.delete())
    else:
        h.insert(cmd)


