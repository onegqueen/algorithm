import copy
N = int(input())
dice = list(map(int,input().split()))

min = 151
min_list = []
if (N>1):
    for i in range(6):
        tmp = []
        tmp.append(dice[i])
        for j in range(i+1,6):
            if(i+j==5):continue
            else:tmp.append(dice[j])
            for k in range(j+1,6):
                if((j+k==5)or(i+k==5)):continue
                else:tmp.append(dice[k])
                tmp_sum = sum(tmp)
                if(tmp_sum<min):
                    min=tmp_sum
                    min_list = copy.deepcopy(tmp)
                #print(i,j,k,":",min_list)
                del tmp[-1]
            del tmp[-1]
    
    min_list.sort()
    three_sides = sum(min_list)
    two_sides = min_list[0]+min_list[1]
    one_sides = min_list[0]

    result = (three_sides*4)+(two_sides*((N-2)*8+4))+(one_sides*((((N-2)**2)*5)+(N-2)*4))
else:
    dice.sort()
    del dice[-1]
    result = sum(dice)
print(result)