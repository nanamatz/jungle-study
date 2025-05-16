T = int(input())

for _ in range(T):
    n,test_case = list(map(str,input().split()))
    n = int(n)
    for i in range(len(test_case)):
        for j in range(n):
            print(test_case[i],end="")
    print()