n,r,c = map(int,input().split())

def z(n, r, c):
    if n == 0:
        return 0

    half = 2 ** (n - 1)
    size = half ** 2

    if r < half and c < half:
        quad = 0
        r = r
        c = c
    elif r < half and c >= half:
        quad = 1
        r = r
        c = c-half
    elif r >= half and c < half:
        quad = 2
        r = r-half
        c = c
    else:
        quad = 3
        r = r-half
        c = c-half
    return quad * size + z(n-1,r,c)
    
print(z(n,r,c))
