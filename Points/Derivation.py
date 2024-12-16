#Python 推导式是一种独特的数据处理方式，可以从一个数据序列构建另一个新的数据序列的结构体

#列表(list)推导式
import random
#生成指定范围的数值列表
list1=[random.randint(1,100) for i in range(10)]
print(list1)
#推导式创建二维列表
list1=[[random.randint(1,100) for x in range(5)]for y in range(3)]
print(list1)
print('\n')
for i in range(3):
    for j in range(5):
        if j == 4:
            print(list1[i][j])
        else:
            print(list1[i][j],end=' ')
print('\n')

#生成一个包含10个随机整数的列表，这些整数位于1到100之间，并且列表中的任何元素都不等于38
list2=[random.randint(1, 100) for _ in range(10)]
for i in range(len(list2)):
    while list2[i] == 38:       #检查数值，若等于38重新生产
        list2[i] = random.randint(1, 100)
print(list2)
#list5=[random.randint(1,100) for i in range(10) if i not in [38]]
#print(list5)

#根据已知列表生成指定需求的列表
price=[500,1000,2000,5000,10000]
list3=[int(i*0.5) for i in price]
print(list3)
#从已知列表筛选符合条件的元素组成新列表
num=[13,25,34,55,100,10,34,21,59,18]
list4=[i for i in num if i%5 == 0]
print(list4)
print('\n')


#元组推导式（生成器表达式）
#元组推导式与列表推导式在外观上只相差 () []
tup1=(random.randint(1,100) for i in range(5))
print(tup1)         #这里输出的是一个生成器对象
tup1=tuple(tup1)    #类型转换
print(tup1)
#tup2=(random.randint(1,100) for _ in range(5))
#for i in range(len(tup2)):                     ##TypeError: object of type 'generator' has no len()，len()函数不能用于生成器对象
#    while tup2[i] == 38:                       #为了实现代码的预期功能，应该使用列表而不是生成器对象
#        tup2[i] = random.randint(1,100)
tup2=(i for i in range(5))
for i in range(5):
    print(tup2.__next__(),end=' ')
print(tuple(tup2),len(tuple(tup2)))         #遍历后原生成器对象已经不存在了
tup3=(i for i in range(5))
for i in range(5):
    print(i,end=' ')
print(tuple(tup2),len(tuple(tup2)))         #与上文同理
print('\n')


#字典推导式
#使用 range 函数
dict1={f'<{i+1}>':random.randint(1,100) for i in range(5)}
print(dict1)
#使用已知列表
list1=['web','misc','crypto','reserve','pwn','AI','blockchain']
list2=['网页安全','安全杂项','密码学','逆向工程','二进制安全','人工智能安全','区块链安全']

dict2={i+1:program for i,program in enumerate(list1)}     #enumerate 函数用于将一个可迭代对象（如列表）组合为一个索引序列，同时列出数据和数据下标
print(dict2)
#多个列表映射转换
CTF={i:j for i,j in zip(list1,list2)}
print(CTF)
print('\n')


#集合推导式
set1={random.randint(1,100) for i in range(5) if not i in [38]}     #当 i 不等于38时条件为真
print(set1)         #由于集合是无序的且不允许重复元素，所以最终生成的集合中可能会有少于5个元素
set2={2**i for i in [1,2,3,4,5,6,7,8]}
print(set2)