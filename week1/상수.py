a,b = list(map(str,input().split()))

rev_a = []
rev_b = []
for i in reversed(range(len(a))):
    rev_a.append(int(a[i]))
    rev_b.append(int(b[i]))


result_a = 0
result_b = 0
for i in range(3):
    result_a += (10 ** (2-i)) * rev_a[i]
    result_b += (10 ** (2-i)) * rev_b[i]

print(max(result_a,result_b))