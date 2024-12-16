#直接初始化
list1=[[1,2,3,4,5],
       [2,3,4,5,6],
       [3,4,5,6,7]]
print(list1)
for i in range(3):
    for j in range(5):
        if j == 4:
            print(list1[i][j])
        else:
            print(list1[i][j],end=' ')
print('\n')

#嵌套循环初始化
list2=[]
for i in range(3):
    list2.append([])
    for j in range(5):
        list2[i].append(j)
print(list2)
for i in range(3):
    for j in range(5):
        if j == 4:
            print(list2[i][j])
        else:
            print(list2[i][j],end=' ')
print('\n')

#推导式初始化
list3=[[i for i in range(5)] for j in range(3)]
print(list3)
for i in range(3):
    for j in range(5):
        if j == 4:
            print(list3[i][j])
        else:
            print(list3[i][j],end=' ')
import random
list4=[[random.randint(1,100) for x in range(5)] for y in range(3)]
print(list4)
for i in range(3):
    for j in range(5):
        if j == 4:
            print(list4[i][j])
        else:
            print(list4[i][j],end=' ')