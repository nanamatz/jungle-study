n = int(input())

arr = [[None]*n]*n

for i in range(n):
    arr[i] = list(map(int,input().split()))

blue = 0
white = 0

def color_paper(n,i,j):
    global blue
    global white

    if n == 1:
        if arr[i][j] == 1:
            blue += 1
        else:
            white += 1
        return
    
    sum_arr = n ** 2
    total = 0

    for row in range(i,n+i):
        for col in range(j,n+j):
            total += arr[row][col]
    

    if total == 0:
        white += 1
    elif total == sum_arr:
        blue += 1
    else:
        color_paper(n//2,i,j)  #1사
        color_paper(n//2,i,j+n//2)  #2사
        color_paper(n//2,i+n//2,j)  #3사
        color_paper(n//2,i+n//2,j+n//2)  #4사

color_paper(n,0,0)

print(white)
print(blue)