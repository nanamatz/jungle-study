a,b,c = map(int,input().split())

def merge(b):
        return (a ** b)        
def partition(b):
    if b >= 1:
        if b % 2 == 0:
            partition(b//2)
            return ((merge(b//2)**2) % c)
        else:
            partition(b//2)
            return ((merge(b//2)**2)*a % c)

def zegop(a,b):
    if b == 0:
         return 1
    result = (zegop(a,b//2)**2)%c
    if b % 2 == 1:
        result = result*a
    return result
result = zegop(a,b)%c

if result == None:
    print(a % c)
else:
    print(result)
