n = int(input())
def Merge(list,left,mid,right):
    sorted_list = [None] * n
    i = left
    j = mid+1
    k = left
    while(i<=mid and j <=right):
        if list[i] < list[j]:
            sorted_list[k] = list[i]
            i+=1
        else:
            sorted_list[k] = list[j]
            j+=1
        k+=1
    if i > mid:
        for index in range(j,right+1):
            sorted_list[k] = list[index]
            k+=1
    else:
        for index in range(left,mid+1):
            sorted_list[k] = list[index]
            k+=1
    return sorted_list

def MergeSort(list,left,right):
    if left < right:
        mid = left + (right - left) // 2
        MergeSort(list,left,mid)
        MergeSort(list,mid+1,right)
        list = Merge(list,left,mid,right)
    return list
def PrintArray(list):
    for i in range(list):
        print(f'{i} ',end="")
arr = [None] * n
for i in range(n):
    arr[i] = int(input())
arr = MergeSort(arr,0,n-1)
PrintArray(arr)
