def is_hansoo(num_list): #리스트로 받아옴
    if len(num_list) < 3:
        return True
    num_sum = len(num_list) * (int(num_list[0]) + int(num_list[len(num_list)-1])) // 2 #등차수열 합 공식 일반항
    if len(num_list) == 3: #홀수 일 때 일반항으로 구한 합과 비교
        if int(num_list[1]) * 3 == num_sum: #홀수일 때 합공식 적용 
            return True
        else:
            return False
    else:
        if int(num_list[0]) + int(num_list[3]) == int(num_list[1]) + int(num_list[2]): #짝수일 때 등차수열 합 특징 이용
            return True
        else:
            return False

n = int(input())
cnt = 0
for i in range(1,n+1):
    i = str(i)
    if is_hansoo(list(i)):
       cnt += 1

print(cnt)
     
