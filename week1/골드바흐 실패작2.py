import sys

def make_prime_list(gold_num):
    prime_list = []
    for i in range(2,gold_num):
        flag = True
        for j in range(2,i):
            if i % j == 0:
                flag = False
                continue
        if flag:
            prime_list.append(i)
    return prime_list

T = int(sys.stdin.readline())

for _ in range(T):
    gold_num = int(sys.stdin.readline())

    prime_list = make_prime_list(gold_num)

    min_gap = 1000000
    prime = 0
    prime_pair = 0

    for i in prime_list:
        a = gold_num - i
        for j in prime_list:
            if a + j == gold_num:
                b = j
                if min_gap > abs(a-b):
                    min_gap = abs(a-b)
                    prime = a
                    prime_pair = b
    print(f'{prime_pair} {prime}')

# def find_pair(size):
#     for i in range(size):
#         prime = gold_num - prime_list[i]
#         if not prime in prime_list:
#             continue
#         pair = 0
#         for j in range(len(prime_list)):
#             if prime_list[j] + prime == gold_num:
#                 pair = prime_list[j]
#                 continue
#     if pair != 0:
#         print(f'{pair} {prime}')


    # if len(prime_list) % 2 == 0:# 절반 나눠서 계산 페어 연산이기 때문에 다 안해도 되니까
    #     size = len(prime_list) // 2  
    # else:
    #     size = len(prime_list) // 2 + 1
    # find_pair(size)        

