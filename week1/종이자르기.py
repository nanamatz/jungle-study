
garo,sero = list(map(int,input().split()))
num = int(input())
x_list = []
y_list = []
x_index_list = [0]
y_index_list = [0]

for _ in range(num):
    flag,index = list(map(int,input().split()))
    if flag: #세로
        x_index_list.append(index)
    else:
        y_index_list.append(index)

if x_index_list:
    x_index_list.sort(reverse=True)
    for i in x_index_list:
        x = garo - i
        garo = i
        x_list.append(x)
    x = max(x_list)
else:
    x = garo


if y_index_list:
    y_index_list.sort(reverse=True)
    for i in y_index_list:
        y = sero - i
        sero = i
        y_list.append(y)
    y = max(y_list)
else:
    y = sero

print(x * y)      

    

