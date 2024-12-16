#算数运算符
print('2+3 =',2+3)
print('2-3 =',2-3)
print('2*3 =',2*3)
print('2/3 =',2/3)
print('3%2 =',3%2)
print('2**3 =',2**3)    #求幂
print('3//2 =',3//2)    #取整相除（取小）
print('-3//2 =',-3//2)

#比较运算符
#返回值为 bool 类型
print(101==5)
print(101!=5)
print(101>5)
print(101<5)
print(101>=5)
print(101<=5)

#赋值运算符
a=5;b=6
c=a+b
print('c = a+b =>',c)
c+=a
print('c+=a =>',c)
c-=a
print('c-=a =>',c)
c*=a
print('c*=a =>',c)
c/=a
print('c/=a =>',c)
c%=b
print('c%=a =>',c)
c**=a
print('c**=a =>',c)
c//=b
print('c//=a =>',c)
#海象运算符
#在表达式中同时进行赋值和返回赋值的值 Python3.8 版本新增运算符
#用于简化循环条件或表达式中的重复计算
a=5
if a>0:         #传统写法
    print(a,'> 0')

if (a:=5)>0:    #海象运算符  ##(a:=5)将变量 a 赋值为 5，同时返回这个赋值结果
    print(a,'> 0')

#位运算符
a=60                    #60=0011 1100
b=13                    #13=0000 1101
print('a&b =',a&b)      #12=0000 1100   按位与
print('a|b =',a|b)      #61=0011 1101   按位或
print('a^b =',a^b)      #49=0011 0001   按位异或
print('~a =',~a)       #-61=1100 0011   按位取反
print('a<<1 =',a<<1)   #120=0111 1000   左移运算符   （*2）
print('a>>1 =',a>>1)    #30=0001 1110   右移运算符   （//2）

#逻辑运算符
#x or y  布尔"或" - 如果 x 是 True，它返回 x 的值，否则它返回 y 的计算值
print('True or False =',True or False)
print('5 or 1 =',5 or 1)
print('False or True =',False or True)
print('1 or 5 =',1 or 5)
#x and y 布尔"与" - 如果 x 为 False，x and y 返回 x 的值，否则返回 y 的计算值
print('True and False =',True and False)
print('5 and 1 =',5 and 1)
print('False and True =',False and True)
print('1 and 5 =',1 and 5)
#x not y 布尔"非" - 如果 x 为 True，返回 False 。如果 x 为 False，它返回 True
print('not True =',not True)
print('not False =',not False)
print('not 1 =',not 1)
print('not 1 and 5 =',not 1 and 5)
print('not 1 or 5 =',not 1 or 5)

#成员运算符
#测试序列包括字符串，列表或元组
#in 如果在指定的序列中找到值返回 True，否则返回 False；not in 反之
list1=[1,2,3,4,5]
a=10
if a in list1:
    print('a in list')
else:
    print('a not in list')

dict1={'title':'Security','author':'VIRTUALGUARD','ID':101}
val=101
key='title'
if val in dict1.values():
    print(val,'in dict1')
else:
    print(val,'not in dict1')
if key in dict1.keys():
    print(key,'in dict1')
else:
    print(key,'not in dict1')

tup=(101,'VIRTUAL','Security')
elem='101'
if elem in tup:
    print(elem,'in tup')
else:
    print(elem,'not in tup')

#运算符优先级
#https://www.runoob.com/python3/python3-basic-operators.html#ysf8

#not > and > or
print(not False and True)
print(True or False and False)