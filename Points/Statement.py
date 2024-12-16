#if 条件控制语句实现闰年判断
#y=int(input('\nInput the year:'))
y=2024
if y%4==0 and y%100!=0 or y%400==0:
    print('{} is a leap year'.format(y))
else:
    print('Not leap year')

#if 嵌套
#n=int(input('\nInput a number:'))
n=6
if n%2==0:
    if n%3==0:
        print(f'{n}%2==0 and {n}%3==0')
    else:
        print(f'{n}%2==0 and {n}%3!=0')
else:
    if n%3==0:
        print(f'{n}%2!=0 and {n}%3==0')
    else:
        print(f'{n}%2!=0 and {n}%3!=0')

#match 分支
#Python 3.10 增加了 match...case 的条件判断，类似于 C 中的 switch...case
def http_status(code):
    #简单的值匹配
    match code:
        case 200:
            return 'OK'
        case 302:
            return 'Found'
        case 400:
            return 'Bad Request'
        case 401:
            return 'Unauthorized'
        case 404:
            return 'Not Found'
        case 500:
            return 'Internal Server Error'
        case _:
            return 'Unknown Error'
#status=int(input('\nInput the status:'))
status=500
print(http_status(status))

def matchtest(item):
    #使用变量
    match item:
        case (x,y):
            if x == y:
                print(f'匹配到相等的元组: {item}')
            else:
                print(f'匹配到元组: {item}')
        case _:
            print('Other')
matchtest((5,5))
matchtest((5,6))
matchtest('text')
matchtest(5)

class Circle:
    def __init__(self, radius):
        self.radius = radius
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
def match_shape(shape):
    #类型匹配
    match shape:
        case Circle(radius=1):
            print("匹配到半径为1的圆")
        case Rectangle(width=1, height=2):
            print("匹配到宽度为1，高度为2的矩形")
        case _:
            print("匹配到其他形状")
match_shape(Circle(radius=1))          # 输出: 匹配到半径为1的圆
match_shape(Rectangle(width=1, height=2)) # 输出: 匹配到宽度为1，高度为2的矩形
match_shape("other")                    # 输出: 匹配到其他形状
print('\n')

#while 循环
sum=0
counter=1
while counter<=100:
    sum+=counter
    counter+=1
print('1+2+3+...+100={}'.format(sum))

#while 循环使用 else 语句
i=0
while i<5:
    print('{}<5'.format(i))
    i+=1
else:
    print('{}>=5'.format(i))
print('\n')

#for 循环
#for 循环可以遍历任何可迭代对象，如一个列表或者一个字符串
CTF=['web','misc','crypto','reverse','pwn']
for program in CTF:
    print(program)
print('\n')

for letter in 'VIRTUAL':
    print(letter)

#for...else
for n in CTF:
    print(n)
else:
    print('That\'s all')
print('\n')

#range 函数
list1=list(range(1,6))
list2=list(range(5))
print(list1,list2)

for i in range(5):
    print(i,end=' ')
print('\n')
for i in range(1,6):
    print(i,end=' ')
print('\n')
for i in range(0,26,5):
    print(i,end=' ')
print('\n')
for i in range(-10,-100,-20):
    print(i,end=' ')
print('\n')
CTF=['web','misc','crypto','reverse','pwn']
for n in range(len(CTF)):       #结合 range() 和 len() 函数以遍历一个序列的索引
    print(n+1,CTF[n],end=' ')
print('\n')

#break 和 continue 语句
i=0
while i<5:
    i+=1
    if i==2:
        break
    print(i,end=' ')
print('\n')
i=0
while i<5:
    i+=1
    if i==2:
        continue
    print(i,end=' ')
print('\n')
for l in 'VIRTUAL':
    if l=='T':
        break
    print(l,end=' ')
print('\n')
for l in 'VIRTUAL':
    if l=='T':
        continue
    print(l,end=' ')
print('\n')

#pass 语句
#pass是空语句，是为了保持程序结构的完整性
#pass 不做任何事情，一般用做占位语句
for letter in 'VIRTUAL':
    if letter == 'T':
        pass
        print('执行 pass 块')
    print(f'当前字母:{letter}')

print("Good bye!")

#素数查找
import math

for num in range(2,100):
    flag = 1
    for x in range(2,int(math.sqrt(num))+1):
        if num%x==0:
            flag=0
            break
    if flag==1:
        print(num,end=' ')
print('\n')

#乘法表
for i in range(1,10):
    for j in range(1,i+1):
        print(f'{j}*{i}={i*j=}',end=' ')
    print('\n')