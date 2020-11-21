
sum_result=0
def new_func():
    result_i = 1
    i = 1
    j = 0
    sum_result=0
    while (abs(result_i)>1.0e-6):
        flag=1.0 if j%2==0 else -1.0
        result_i=flag*1/i
        i=i+3
        j=j+1
        sum_result=sum_result+result_i
    return print('第%s次的结果是%s，合计为%s' %(j,result_i,sum_result))

if __name__ == "__main__":
    new_func()