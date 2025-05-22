t = int(input())

# def sum_123(n,k):
#     if n < 1 or k < 1:
#         return 1
#     return sum_123(n-1,k-1) + sum_123(n-k,k) 실패작
for _ in range(t):
    n = int(input())
    dp = [0] * (n+1)
    for i in range(1,n+1):
        for j in range(1,4):    #현재 정수는 이전 정수 계산값을 전부 더해주면 된다.
            if i > j:
                dp[i] += dp[i-j]
            elif i == j:
                dp[i] += 1
    print(dp[n])
