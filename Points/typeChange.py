#隐藏式类型转换
#对两种不同类型的数据进行运算，较低数据类型（整数）就会转换为较高数据类型（浮点数）以避免数据丢失
num1=123
num2=1.23
num3=num1+num2
print('Type of num1:',type(num1))
print('Type of num2:',type(num2))
print('num3=',num3)
print('Type of num3:',type(num3))
print('\n')

#显式类型转换
num=123
string='456'
#print(num+string)  #TypeError: unsupported operand type(s) for +: 'int' and 'str'
string=int(string)  #显式类型转换 str -> int
print(num+string)
print('\n')

#显式类型转换操作函数
print('int(n,[base]):',end='\n')    #整型
print(int())
print(int(2.5))
print(int('0xa',base=16))   #base -- 进制数，默认十进制
print(int('010',8))    #将 010 转换为十进制整数

print('float(n):',end='\n')  #浮点型
print(float())
print(float(2))

print('complex(real,[imag]):',end='\n') #创建一个复数
print(complex())
print(complex(1,5))
print(complex(1))
print(complex('1'))
print(complex('1+2j'))      #注意：这个地方在"+"号两边不能有空格，也就是不能写成"1 + 2j"，应该是"1+2j"，否则会报错

print('str(object=''):',end='\n')   #字符串（注重可读性）
print(str())
print(str(101))
print(type(str(101)))
dict1={'name':'VIRTUALGUARD','code':101}
print(str(dict1))                   #str() 返回 dict1 的string格式
print(type(dict1))
print(type(str(dict1)))

print('repr(object):',end='\n')    #表达式字符串（注重精确性和可重构性）
#print(repr())                     ##TypeError: repr() takes exactly one argument (0 given)
print(repr(101))
print(type(repr(101)))
dict1={'name':'VIRTUALGUARD','code':101}
print(repr(dict1))                   #str() 返回 dict1 的string格式
print(type(dict1))
print(type(repr(dict1)))

print('eval(expression,[globals],[locals]):',end='\n')
#eval() 函数将字符串 expression 解析为 Python 表达式，并在指定的命名空间中执行它
#globals -- 变量作用域，全局命名空间，如果被提供，则必须是一个字典对象
#locals -- 变量作用域，局部命名空间，如果被提供，可以是任何映射对象
print(type('2+3*5'))
print(eval('2+3*5'))            #执行简单表达式
print(type(eval('2+3*5')))
r=15
print(eval('r+10'))             #执行变量引用
namespace={'a':3,'b':2}
print(eval('a+b',namespace))    #在指定命名空间执行表达式

print('tuple(iterable):',end='\n')
#tuple 函数将可迭代系列（如列表）转换为元组
#iterable -- 要转换为元组的可迭代序列
list1=['VIRTUAL','GUARD',101]
print(list1)
print(type(list1))
print(tuple(list1))
print(type(tuple(list1)))

print('list(seq):',end='\n')
#list() 方法用于将元组或字符串转换为列表
#seq -- 要转换为列表的元组或字符串
tup=('VIRTUAL','GUARD',101)
print(tup)
print(type(tup))
print(list(tup))          #将元组转换为列表
print(type(list(tup)))
string='VIRTUALGUARD'
print(string)
print(type(string))
print(list(string))       #将字符串转换为列表
print(type(list(string)))

print('set([iterable]):',end='\n')
#set() 函数创建一个无序不重复元素集，可进行关系测试，删除重复数据，还可以计算交集、差集、并集等
#iterable -- 可迭代对象对象
print(set('VIRTUAL'),set('GUARD'))
print(set('Google'))        #重复对象被删去
s=set('google')
t=set('edge')
print(s&t,s|t,s-t)          #集合运算

print('dict(**kwargs)'
      'dict(mapping,**kwargs)'
      'dict(iterable,**kwargs):',end='\n')
#dict() 函数用于创建一个字典
#**kwargs -- 关键字
#mapping -- 元素的容器，映射类型（Mapping Types）是一种关联式的容器类型，它存储了对象与对象之间的映射关系
#iterable -- 可迭代对象
print(dict())                           #空字典
print('dict1 =',dict(a='a',b='b',c='c'))          #传入关键字赖构造字典
print('dict2 =',dict(zip(['title','author','ID'],['Security','VIRTUALGUARD',101])))   #映射函数方式来构造字典，zip() 创建可迭代对象
print('dict3 =',dict([('one',1),('two',2),('three',3)]))                              #可迭代对象方式来构造字典
dict4=dict({'four':4,'five':5},six=6)       #映射
print('dict4 =',dict4)
dict5=dict([('x', 5), ('y', -5)], z=8)      #设置关键字参数
print('dict5 =',dict5)

print('frozenset([iterable]):',end='\n')
#frozenset() 返回一个冻结的集合，冻结后集合不能再添加或删除任何元素
#iterable -- 可迭代的对象，比如列表、字典、元组等等
print(frozenset(range(10)))                 #生成一个不可变集合
print(frozenset(['VIRTUAL','GUARD',101]))   #创建一个不可变集合


print('chr(i):',end='\n')
#chr() 用一个范围在 range（256）内的（就是0～255）整数作参数，返回一个对应的 ASCII 字符
#i -- 可以是10进制也可以是16进制的形式的整数
print(chr(0x30),chr(0x31),chr(0x61))
print(chr(48),chr(49),chr(97))
print(type(chr(65)))

print('ord(c):',end='\n')
#ord() 函数是 chr() 函数（对于8位的ASCII字符串）或 unichr() 函数（对于Unicode对象）的配对函数，它以一个字符（长度为1的字符串）作为参数，返回对应的 ASCII 数值(十进制数)，或者 Unicode 数值，如果所给的 Unicode 字符超出了你的 Python 定义范围，则会引发一个 TypeError 的异常
#c -- 字符
print(ord('A'),ord('a'),ord('0'),ord('1'))

print('hex(i):',end='\n')
#hex() 函数用于将10进制整数转换成16进制，以字符串形式表示
#i -- 10进制整数
print(hex(5),hex(16),hex(0x1e),hex(-255))
print(type(hex(5)))

print('oct(i):',end='\n')
#oct() 函数将一个整数转换成 8 进制字符串
#Python3.x 版本的 8 进制以 0o 作为前缀表示
#i -- 整数
print(oct(5),oct(8),oct(0x1e),oct(-255))
print(type(oct(5)))

print('bin(i):',end='\n')
#oct() 函数将一个整数转换成 2 进制字符串
#Python3.x 版本的 2 进制以 0b 作为前缀表示
#i -- 整数
print(bin(5),bin(8),bin(0x1e),bin(-255))
print(type(bin(5)))