tup1=('VIRTUAL','GUARD','Benjamin',101)
tup2=(1,2,3,4,5)
tup3='web','crypto','misc','pwn','reverse'
print(type(tup1),type(tup2),type(tup3))
tup=()          #空元组
print(type(tup))
#元组中只包含一个元素时，需要在元素后面添加逗号 , ，否则括号会被当作运算符使用
tup4=('CTF',)
tup5='ICT',
tup=('CTF')
tups='ICT'
print(type(tup4),type(tup5))
print(type(tup),type(tups))

#访问元组
print(tup3)
print(tup3[0])
print(tup2[1:3])

#元组中的元素值是不允许修改的，但我们可以对元组进行连接组合
tup6=tup4+tup3
print(tup6)

#元组中的元素值是不允许删除的，但我们可以使用del语句来删除整个元组
print(tup5)
del tup5
#print(tup5)        ##NameError: name 'tup5' is not defined.

#元组运算符
print(len(tup6))        #计算元素个数

print(tup1+tup4)        #连接，c 就是一个新的元组，它包含了 a 和 b 中的所有元素
tup1+=tup4
print(tup1)

print(tup1*2)           #复制

print('VIRTUAL' in tup1)#查找

for elem in tup1:       #迭代
    print(elem,end=' ')

#元组截取与其他支持引索和切片的序列异曲同工，这里不再赘述

#元组内置函数
print(len(tup1))        #计算元组元素个数

print(max(tup3))        #返回元组中元素最大值
print(max(tup2))

print(min(tup3))        #返回元组中元素最小值
print(min(tup2))

list1=['web','crypto','misc','pwn','reverse']
print(tuple(list1))     #将可迭代序列（这里是列表）转换为元组

#元组的不可变性
print(tup3[0])
#tup3[0]='CTF'          #TypeError: 'tuple' object does not support item assignment
#所谓元组的不可变指的是元组所指向的内存中的内容不可变
print(id(tup3))
tup3=("CTF",)           #修改前后地址不一致
print(id(tup3))         #重新赋值的元组 tup，绑定到新的对象了，不是修改了原来的对象