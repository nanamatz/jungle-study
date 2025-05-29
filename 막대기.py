from collections import deque
import sys
input = sys.stdin.readline
n = int(input())
st = deque()

for _ in range(n):
    st.append(int(input()))

standard = st.pop()
cnt = 1
for _ in range(n-1):
    i = st.pop()
    if i > standard:
        cnt += 1
        standard = i
    

print(cnt)