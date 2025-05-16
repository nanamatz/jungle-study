T = int(input())

for i in range(T):
    ox_list = input()
    sum = 0
    combo = 0
    for j in range(len(ox_list)):
        if ox_list[j] == 'X':
            combo = 0
            continue
        combo += 1
        sum += combo
    print(sum)

    


        
