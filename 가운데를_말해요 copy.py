import sys
input = sys.stdin.readline

class Heap():
    def __init__(self,capacity):
        self.size = 0
        self.arr = [None] * (capacity + 1)
        self.capacity = capacity
    
    def insert(self,value):
        self.size += 1
        i = self.size
        while(i != 1 and value < self.arr[i//2]):
            self.arr[i] = self.arr[i//2]
            i = i//2
        self.arr[i] = value
        
        
    
    # def delete(self):
    #     if self.size == 0 :
    #         return 0
        
    #     item = self.arr[1]
    #     temp = self.arr[self.size]

    #     self.size -= 1
        
    #     parent = 1
    #     child = 2

    #     while(child <= self.size):

    #         if child < self.size and self.arr[child] > self.arr[child+1]:
    #             child += 1
            
    #         if temp <= self.arr[child]:
    #             break
            
    #         self.arr[parent] = self.arr[child]
    #         parent = child
    #         child *= 2

    #     self.arr[parent] = temp

    #     return item
    

def say_median():
    if heap.size % 2 == 0:
        mid = heap.size // 2
        if heap.arr[mid] > heap.arr[mid + 1]:
            mid += 1
    else:
        mid = heap.size // 2 + 1

    return heap.arr[mid]

n = int(input())

heap = Heap(n)
for _ in range(n):
    heap.insert(int(input()))
    print(say_median())
