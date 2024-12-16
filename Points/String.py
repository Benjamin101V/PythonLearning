string1='VIRTUAL'
string2="GUARD"

#访问字符串中的值
print(string1[0])
print(string2[1:5])

#字符串更新
print(string1[:7]+string2)
print(string1[:7]+'GUARD')

#转义字符
print('line1 \
       line2 \
       line3')      # \ 续行符

print('\\')         #输出反斜杠 \

print('\'')         #输出单引号 ' ,双引号 " 同理

print('\a')         #响铃符

print('Hello,\bworld!')     #退格符

print('\000')       #空
print('Hello\000World')

print('\n')         #换行符

print('VIRTUAL\vGUARD')     #纵向制表符
print('VIRTUAL\tGUARD')     #横向制表符

print('VIRTUALGUARD\rREALITY')      #回车，将 \r 后面的内容移到字符串开头，并逐一替换开头部分的字符，直至将 \r 后面的内容完全替换完成
print('Hello\rworld')               #这里的实例会全部替换

print('Hello\fworld')       #换页符

print("\110\145\154\154\157\40\127\157\162\154\144\41")     #八进制数
print('\012')   #换行

print("\x48\x65\x6c\x6c\x6f\x20\x57\x6f\x72\x6c\x64\x21")
print('\x0a')   #换行
#使用 \r 实现百分比进度
#import time

#for i in range(101):
#    print("\r{:3}%".format(i), end=' ')
#    time.sleep(0.05)
print('\n')

#字符串格式化
#在 Python 中，字符串格式化使用与 C 中 sprintf 函数一样的语法
print('我叫 %s 今年 %d 岁!',('cc',10))
#https://www.runoob.com/python3/python3-string.html

#Python2.6 开始，新增了一种格式化字符串的函数 str.format()，它增强了字符串格式化的功能
#基本语法是通过 {} 和 : 来代替以前的 %
#format 函数可以接受不限个参数，位置可以不按顺序
print('{0}{1}'.format('VIRTUAL','GUARD'))  #设置指定位置
print('{0}{1} {0}'.format('VIRTUAL','GUARD'))  #设置指定位置
print('{} {}'.format('VIRTUAL','GUARD'))  #不设置指定位置，使用默认位置

print('title:{title},author:{author},ID:{ID}'.format(title='Security',author='VIRTUALGUARD',ID=101))
list1=['Security','VIRTUALGUARD',101]
print('title:{0[0]},author:{0[1]},ID:{0[2]}'.format(list1))     #通过列表引索设置参数 #引索前的 '0' 是必须的
dict1={'title':'Security','author':'VIRTUALGUARD','ID':101}
print('title:{title},author:{author},ID:{ID}'.format(**dict1))  #通过字典设置参数
#向 str.format() 传入对象
class AssignValue(object):
    def __init__(self, value):
        self.value = value
my_value = AssignValue(6)
print('value 为: {0.value}'.format(my_value))  # "0" 是可选的
print('\n')

#数字格式化
#https://www.runoob.com/python/att-string-format.html
import math
print('{:.2f}'.format(math.pi))
print('{:+.2f}'.format(math.pi))
print('{:+.3f}'.format(-math.pi))
print('{:0>2d}'.format(5))
print('{:0<5d}'.format(15))
print('{:,}'.format(1000000))
print('{:e}'.format(3141592653589793))
print('{:.2e}'.format(3141592653589793))
print('{:,}'.format(5.000000e+07))
print('{:%}'.format(1/4))
print('{:.2%}'.format(0.25))
print('{:>5d}'.format(5))   #右对齐，宽度为5
print('{:<5d}'.format(5))   #左对齐，宽度为5
print('{:^5d}'.format(5))   #居中，宽度为5
print('{:b}'.format(11))
print('{:d}'.format(11))
print('{:o}'.format(11))
print('{:x}'.format(11))
print('{:#x}'.format(11))
print('{:#X}'.format(11))
print('\n')

para_str = '''这是一个多行字符串的实例
多行字符串可以使用制表符
TAB ( \t )。
也可以使用换行符 [ \n ]。
'''
print (para_str)
#三引号让程序员从引号和特殊字符串的泥潭里面解脱出来，自始至终保持一小块字符串的格式是所谓的WYSIWYG（所见即所得）格式的

#f-string 是 python3.6 之后版本添加的，称之为字面量格式化字符串，是新的格式化字符串的语法
#f-string 格式化字符串以 f 开头，后面跟着字符串，字符串中的表达式用大括号 {} 包起来，它会将变量或表达式计算后的值替换进去
name='VIRTUALGUARD'
print('Hello,%s' % name)
print(f'Hello,{name}')

dict1={'title':'Security','ID':101}
print(f'{dict1["title"]}: {dict1["ID"]}')

n=5
print(f'{n**2}')
print(f'{n*n=}')    #在 Python 3.8 的版本中可以使用 = 符号来拼接运算表达式与结果

#字符串内建函数
#https://www.runoob.com/python/python-strings.html

print(str.capitalize('benjamin'))   #str.capitalize() 将字符串的第一个字母变成大写,其他字母变小写。对于 8 位字节编码需要根据本地环境

