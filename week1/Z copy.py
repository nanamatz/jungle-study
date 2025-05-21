n,r,c = map(int,input().split())
arr = [[0 for col in range(2**n)]for row in range(2**n)]
size = 2**n - 1

def print_2d():
    for i in arr:
        for j in i:
            print(j,end="")
        print()

def z(n,m,i,j):
    if i > size or j > size:    #분리를 안 해도 되는지 모르겠음.
        return
    if not i == 0 and i % 2 == 0:
        unit_dis = 2 ** (2 ** i) # 2 ** (i + 1)과 동일
    else:
        unit_dis = 2
    
    
    
