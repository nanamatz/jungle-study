n = int(input())
array = [None] * n

for i in range(n):
    array[i] = int(input())
for i in range(n):
    j = i
    while(j>0 and array[j-1] > array[j]):
        array[j],array[j-1] = array[j-1],array[j]
        j -= 1
print(array)