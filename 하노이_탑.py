n = int(input())
def n_hanoi(n):
    if n == 1:
        return 1
    return 2 * n_hanoi(n-1) + 1

def hanoi(n,start,temp,dest):
    if n < 1:
        return
    hanoi(n-1,start,dest,temp)
    print(f'{start} {dest}')
    hanoi(n-1,temp,start,dest)

print(n_hanoi(n))
if(n <= 20):
    hanoi(n,'1','2','3')
