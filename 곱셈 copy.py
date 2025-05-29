a, b, c = map(int, input().split())

def power(a, b):
    if b == 0:
        return 1
    half = power(a, b // 2)
    result = (half * half) % c
    if b % 2 == 1:
        result = (result * a) % c
    return result

print(power(a, b) % c)
