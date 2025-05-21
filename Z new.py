n,r,c = map(int,input().split())
arr = [[0 for col in range(2**n)]for row in range(2**n)]
size = 2 ** n - 1

def quad_recursion(x,y,n,i):
    half_x = (2**(n-i)-1)//2+1
    half_y = (2**(n-i)-1)//2+1
    if n < 2:
        return

    if i == n-1:
        print(2**(2**(n-1)))
        return
    
    if ((r <= half_x) and ( c <= half_y)):
        quad = 0
        x = x
        y = y
    elif (r <= half_x) and (c > half_y):
        quad = 1
        x = x
        y = half_y
    elif ((r > half_x) and ( c <= half_y)):
        quad = 2
        x = half_x
        y = y
    else :
        quad = 3
        x = half_x
        y = half_y
    print(quad)
    quad_recursion(x,y,n,i+1)

    return

quad_recursion(0,2**n-1,n,0)
start_cnt = 2**(n+1)
