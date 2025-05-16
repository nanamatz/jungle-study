a = int(input())

rank = "F"
if a >= 90:
    rank = "A"
elif a >= 80:
    rank = "B"
elif a >= 70:
    rank = "C"
elif a >= 60:
    rank = "D"

print(rank)