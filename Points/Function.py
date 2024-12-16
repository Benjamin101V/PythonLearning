def add(a,b):
    print(f'{a}+{b}=',end='')
    return a+b
print(add(1,5))
print('\n')

def string_print(string):
    if type(string)==str:
        print(string)
        return 0
    else:
        print('Invalid Data!')
        return 1
string_print('VIRTUALGUARD')          #传递字符串参数
string_print(5)
print('\n')

#在 python 中，类型属于对象，对象有不同类型的区分，变量是没有类型的
a='VIRTUAL'
print(type('VIRTUAL'),type(a))
a=[1,2,3]
print(type([1,2,3]),type(a))
#变量 a 是没有类型，它仅仅是一个对象的引用（一个指针），可以是指向 List 类型对象，也可以是指向 String 类型对象
#python 中一切都是对象，严格意义我们不能说值传递还是引用传递，我们应该说传不可变对象和传可变对象
