import math
a,b,v = list(map(int,input().split()))

distance = a-b
days = math.ceil(v / distance)
print(days)
days -= b

print(days)