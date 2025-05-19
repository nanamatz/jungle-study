import sys

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False  # 짝수는 2를 제외하고 소수 아님

    # 3부터 √n까지 홀수만 검사
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

t = int(sys.stdin.readline())

for _ in range(t):
    gold_num = int(sys.stdin.readline())

    half = gold_num // 2

    prime = 0
    pair = 0
    flag = False
    for i in range(half,gold_num):
        if is_prime(i):
            prime = i
            for j in range(half+1,1,-1):
                if is_prime(j) and j + prime == gold_num:
                    pair = j
                    flag = True
                    break
        if flag:
            break

        
    
    print(f'{pair} {prime}')
            
    
