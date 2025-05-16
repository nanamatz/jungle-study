import sys
a = int(sys.stdin.readline())


b = sys.stdin.readline()


for i in reversed(range(3)):
    print(a*int(b[i]))

d_hun = int(b[0]) * 100
d_ten = int(b[1]) * 10
d_one = int(b[2])

b = d_hun + d_ten + d_one
print(a*b)

