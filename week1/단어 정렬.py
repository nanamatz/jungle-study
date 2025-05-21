n = int(input())

words = []*n
               
                
for i in range(n):
    word = input().strip()

    if word in words:
        continue
    words.append(word)

words.sort(key=lambda x: (len(x),x))

# sort_by_alp(words)

for word in words:
    print(word)

