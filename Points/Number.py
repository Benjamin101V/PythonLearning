import math
import random

#数学函数
print('abs(-5) =',abs(-5))     #返回数字的绝对值

print('math.ceil(4.5) =',math.ceil(4.5))    #返回数字的上入整数

print('math.exp(1) =',math.exp(1))      #返回 e 的 n 次幂

print('math.fabs(-5)=',math.fabs(-5))   #返回数字绝对值的浮点数形式

print('math.floor(5.9) =',math.floor(5.9))  #返回数字的下入整数

print('math.log(math.e**2) =',math.log(math.e**2))      #对数运算
print('math.log(32,2) =',math.log(32,2))
print('math.log10(100) =',math.log10(100))

print('max(1,3,5,2)',max(1,3,5,2))      #需输入整数，浮点数会报警告
print('min(1,3,5,2)',min(1,3,5,2))
tup=(2,5,7,4)
list1=[3,7,9,2]
print('min(tup) =',min(tup))            #参数可以是序列
print('max(list1) =',max(list1))

print('math.modf(pi) =',math.modf(math.pi))     #返回x的整数部分与小数部分，两部分的数值符号与x相同，整数部分以浮点型表示

print('pow(2,5) =',pow(2,5))    #2**5

print('round(math.pi,2) =',round(math.pi,2))    #返回浮点数 x 的四舍五入值，如给出 n 值，则代表舍入到小数点后的位数，否则默认返回整数
print('round(math.e) =',round(math.e))          #其实准确的说是保留值将保留到离上一位更近的一端

print('math.sqrt(2) =',math.sqrt(2))            #返回数字的平方根
print('math.sqrt(4) =',math.sqrt(4))
print(round(math.sqrt(2),6))
print('\n')


#随机数函数
print(random.choice(range(10)))           #从0到9随机输出一个数字
list2=[5,25,125,625,3125]
tup=(2,4,8,16,32)
print(random.choice(list2))               #参数可以是任意序列
print(random.choice(tup))

print(random.randrange(0,100,5))    #从指定范围内，按指定基数递增的集合中获取一个随机数，基数默认值为 1
print(random.randrange(0,100))

print(round(random.random()))             #随机生成下一个实数，它在[0,1)范围内
print(round(random.random(),3))

random.seed()                       #默认种子生成随机数
print(random.random())
random.seed(5)                      #使用整数 5 作为种子生成随机数
print(random.random())              #多次运行的结果一致
random.seed('VIRTUAL',5)  #使用字符串作为种子生成随机数
print(random.random())              #不必特别去设定seed，Python会帮自动选择seed

list3=[5,25,125,625,3125]
random.shuffle(list3)           #将序列的所有元素随机排序
print(list3)

print(random.uniform(5,25))     #uniform() 方法将随机生成下一个实数，它在 [x,y] 范围内
print(random.uniform(10,1))


#三角函数
print('cos(0) =',math.cos(0))

print('sin(π/2) =',math.sin(math.pi/2))

print('tan(π/4) =',math.tan(math.pi/4))

print('π/2 rad =',math.degrees(math.pi/2),'°')
print('π/4 rad =',math.degrees(math.pi/4),'°')

print('30° =',math.radians(30),'rad')
print('60° =',math.radians(60),'rad')