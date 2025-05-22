n = int(input())
digit = [0,0]
cnt = 0
d_sum = 0

if n < 10:
    digit[0] = 0
    digit[1] = n
else:
    temp = str(n)
    digit[0] = int(temp[0])
    digit[1] = int(temp[1])

while(1):
    cnt += 1

    num1 = digit.pop(0)     
    num2 = digit.pop(0)

    n_sum = num1 + num2
    digit.append(num2)      #[num2,] 상태

    if n_sum >= 10:
        temp = str(n_sum)
        digit.append(int(temp[1])) #두 자리 수이면 뒤에 수를 넣는다.
    else:
        digit.append(n_sum)     #[num2,n_sum] 상태

    a = str(digit[0])
    b = str(digit[1])
    s = a+b

    new_num = int(s)

    if new_num == n:          #n과 동일하면 탈출
        break
print(cnt)

    
    


