#https://www.runoob.com/python3/python3-data-type.html

#数字类型
a,b,c,d=10,2.5,1+5j,True  #同行赋值
print(a,b,c,d,end='\n')
print(type(a),type(b),type(c),type(d),end='\n')
print(isinstance(a,int),isinstance(b,float),isinstance(c,complex),isinstance(d,bool),end='\n')  #使用 isinstance() 判断
'''
type()不会认为子类是一种父类类型。
isinstance()会认为子类是一种父类类型。
'''
class A:
    pass
class B(A):
    pass
print(isinstance(A(),A),type(A())==A,end='\n')
print(isinstance(B(),A),type(B())==A,end='\n')

#del语句删除对象
var_1,var_2=3,6
print(var_1,var_2)
del var_1,var_2
#print(var_1,var_2)  ##提示变量未定义

#数值运算
a=2+3;b=8.5-3;c=5*5;f=10%4
d=10/4  #返回浮点数  #在混合计算时，Python会把整型转换成为浮点数
e=10//4 #返回整数
g=5**2  #乘方
print('2+3=',a,'8.5-3=',b,'5*5=',c,'10/4=',d,'10//4=',e,'10%4=',f,'5**2=',g,end='\n')

#复数
a=1+5j
b=complex(1,-5)
print(a,b)

#字符串
#Python 没有单独的字符类型，一个字符就是长度为1的字符串
string1='VIRTUAL'
print(len(string1))  #输出字符串长度
print(string1)       #从左往右输出字符串
print(string1[0])    #输出第一个字符
print(string1[-1])   #输出最后一个字符（从右往左输出第一个字符串）
print(string1[0:-1]) #从左往右输出至最后一个字符（不包含）
print(string1[0:5])  #从左往右输出至第五个字符（包含）
print(string1[0:5:2])#从左往右输出第五个字符，步长为二
print(string1[::2])  #输出字符串，步长为二
#stringName[头下标:尾下标:步长]
print(string1*2,end='\n')     #将 string1打印两次
print(string1+'GUARD',end='\n')
#Python 字符串不能被改变
string2='VIRTUAL'
#string2[5]='g'       ##TypeError: 'str' object does not support item assignment

#转义字符
print(r'\n')
print('Hello\nWorld!\n')
print(r'Hello\nWorld!\n',end='\n')

#bool类型
a=True
b=False
print(int(a),int(b))    #bool值
print(bool(0),bool(25),bool(-5),bool(''),bool('Python'),bool([]),bool([101,105]))
#bool逻辑运算
print(True or False)
print(True and False)
print(not True)
print('\n')

#List（列表）
a=[1,2,3,4,5,6]
a[0]=101        #与Python字符串不一样的是，列表中的元素是可以改变的
a[2:5]=103,104,105
print(a)
a[2:5]=[]       #将对应的元素（第三个元素至第五个元素）值设置为 []
print(a)

def reverseWords(i):
    # 通过空格将字符串分隔符，把各个单词分隔为列表
    inputWords = i.split(" ")

    # 翻转字符串
    # 假设列表 list = [1,2,3,4],
    # list[0]=1, list[1]=2 ，而 -1 表示最后一个元素 list[-1]=4 ( 与 list[3]=4 一样)
    # inputWords[-1::-1] 有三个参数
    # 第一个参数 -1 表示最后一个元素
    # 第二个参数为空，表示移动到列表末尾
    # 第三个参数为步长，-1 表示逆向
    inputWords = inputWords[-1::-1]

    # 重新组合字符串
    output = ' '.join(inputWords)

    return output


if __name__ == "__main__":
    i = 'I am VIRTUAL'
    rw = reverseWords(i)
    print(rw)
    print('\n')

#Tuple（元组）
#元组（tuple）与列表类似，不同之处在于元组的元素不能修改。元组写在小括号 () 里，元素之间用逗号隔开
tup=(5,1970,'VIRTUAL')
stup=('GUARD',101)
print(tup)
print(tup[0])
print(tup[1:3])
print(tup[2:])
print(stup*2)
print(tup+stup)
tup1 = ()    # 空元组
tup2 = (20,) # 一个元素，需要在元素后添加逗号
not_a_tuple = (42) #这不是一个元组
print('\n')

#Set（集合）
set1={'CTF','Security','SRC','CS','CTF'}
print(set1)     #输出集合，重复的元素被自动去掉
#集合测试
if 'CTF' in set1:
    print('"CTF" is in set1')
else:
    print('"CTF" is not in set1')
#set运算
a=set('VIRTUAL')
b=set('GUARD')
print(a)
print(a-b)      #a和b的差集
print(b-a)      #bhea的差集
print(a|b)      #a和b的并集
print(a&b)      #a和b的交集
print(a^b)      #a和b中不同时存在的元素
print('\n')

#Dictionary（字典）
#列表是有序的对象集合，字典是无序的对象集合。两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取
#字典是一种映射类型，字典用 { } 标识，它是一个无序的 键(key) : 值(value) 的集合
dict1={}
dict1['one']='1-CTF'
dict1[2]='2-Security'
dict2={'name':'Benjamin','designation':'VIRTUALGUARD','code':101}
print(dict1)            #输出整个字典
print(dict1['one'])     #输出键为 'one' 的值
print(dict1[2])         #输出键为 '2' 的值
print(dict2)            #输出整个字典
print(dict2.keys())     #输出所有的键
print(dict2.values())   #输出所有的值
#使用 dict() 构造函数构造字典
dict3=dict([('title','Security'),('author','VIRTUALGUARD'),('ID',101)])
dict4=dict(Secrity=1,CTF=2,Programing=3)
print(dict3)
print(dict4)
#字典推导式构造字典
dict5={n:n**2 for n in range(11,26)}
print(dict5)
print(dict5[25])
print('\n')

#bytes 类型
#在 Python3 中，bytes 类型表示的是不可变的二进制序列（byte sequence）
string=bytes('VIRTUAL',encoding='utf-8')
print(string)
#与字符串类型类似，bytes 类型也支持许多操作和方法，如切片、拼接、查找、替换等等。同时，由于 bytes 类型是不可变的，因此在进行修改操作时需要创建一个新的 bytes 对象
s=b'GUARD'
t=s[1:3]    #对 s 进行切片操作
x=string+s  #对 string 和 s 进行拼接操作
print(t)
print(x)
#需要注意的是，bytes 类型中的元素是整数值，因此在进行比较操作时需要使用相应的整数值
print(type(string[0]))
if string[0]==ord('V'):
    print('The first element is',string[0],'(ASCII)')