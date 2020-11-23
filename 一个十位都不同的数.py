# a可以被1整除
# ab可以被2整除
# abc可被3整除
# abcd可被4整除
# abcde可被5整除
# abcdef可被6整除
# abcdefg可被7整除
# abcdefgh可被8整除
# abcdefghi可被9整除
# abcdefghij可被10整除
# 且abcdefghij 各不相同的，求abcdefghij

# b是偶数，且b为2 4 6 8
# e与j是0或5


import random
import datetime
starttime = datetime.datetime.now()
num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

while (num != []):
    sum_num = 0
    num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    for j in range(10):
        i = random.choices(num)[0]
        sum_num=sum_num*10+i
        if sum_num%(j+1)==0 and num != []:
            num.remove(i)
        else:
            break
print("i=%s,j=%s,sum_num=%s,num=%s" %(i,j,sum_num,num))

endtime = datetime.datetime.now()
print("整体耗时：%sseconds" %(endtime - starttime))
