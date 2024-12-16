import keyword
import sys

#https://www.runoob.com/python3/python3-basic-syntax.html

#第一个Python程序
print("Hello,World!\n")

#Python保留字
print(keyword.kwlist)
print('\n')

'''
这是一行注释
这是一行注释
'''

#字符串
string="12345"
print(len(string))  #输出字符串长度
print(string)       #输出字符串
print(string[0])    #输出第一个字符
print(string[-1])   #输出最后一个字符
print(string[0:-1]) #从左往右输出至最后一个字符（不包含）
print(string[0:4])  #从左往右输出至第四个字符
print(string[0:4:2])#从左往右输出第四个字符，步长为二
paragraph="""
这是一个段落
可以由多行组成
"""
print(paragraph)
print('\n')

#输出转义字符
print(r'\n')
print('Hello\nWorld!\n')
print(r'Hello\nWorld!\n')

#等待用户输入
input("\n\n按下enter继续")

#多语句同行
x='12345';sys.stdout.write(x)
print('\n')

#print不换行输出
string1='VIRTUAL'
string2='GUARD'
string3='benjamin_c'
string4='qq.com'
print(string1,end='')
print(string2,end='')
print('\n')
print(string3,end='@')
print(string4,end='')
print('\n')


#import [module] & from [module] import [func1],[func2],[func3],...
import sys
print('============ Python import mode ==============')
print('命令行参数为:')
for i in sys.argv:
    print(i)
print('\nPython 路径为:',sys.argv,end='\n')

from sys import argv,path
print('============ Python import mode ==============')
print('\nPython 路径为:',path,end='\n')