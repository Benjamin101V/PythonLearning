dict1={'title':'Security','author':'VIRTUALGURAD{}','ID':101}
emptyDict1={}
emptyDict2=dict()
print(dict1,len(dict1))
print(emptyDict1,len(emptyDict1))
print(emptyDict2,len(emptyDict2))

list1=['web','misc','crypto','pwn','reverse']
list2=['网页安全','安全杂项','密码学','二进制安全','逆向工程']
CTF1=dict(zip(list1,list2))          #通过映射函数创建字典
print(CTF1)

CTF2=dict(web='网页安全',misc='安全杂项',crypto='密码学',pwn='二进制安全',reverse='逆向工程')   #通过给定关键字参数创建字典
print(CTF2)

CTF3=dict.fromkeys(list1)           #通过 fromkeys 方法创建值为空的字典
print(CTF3)

tup=('web','misc','crypto','pwn','reverse')
CTF4={tup:list2}                    #通过已存在的元组和列表创建字典（效果和前面并不一样）
print(CTF4)
tup=list(tup)
#CTF4={tup:list2}                    ##TypeError: unhashable type: 'list'

print(CTF1['web'])
print(CTF1.get('web','Invalid Data'))
print(CTF1.get('ICT','Invalid Data'))
print('\n')

for item in CTF1:
    print(item,end=' ')
print('\n')
for item in CTF1.items():
    print(item,end=' ')
print('\n')
for key,value in CTF1.items():
    print(f'{key}:{value}',end='\t')
print('\n')

dict1['subject']='information security'
print(dict1)
dict1['ID']=105
print(dict1)
del dict1['ID']
print(dict1)

#字典值可以是任何的 python 对象，既可以是标准的对象，也可以是用户定义的，但键不行
#不允许同一个键出现两次。创建时如果同一个键被赋值两次，后一个值会被记住
tinydict = {'Name': 'Runoob', 'Age': 7, 'Name': '小菜鸟'}
print("tinydict['Name']: ", tinydict['Name'])
#键必须不可变，所以可以用数字，字符串或元组充当，而用列表就不行
tup=('web','misc','crypto','pwn','reverse')
CTF4={tup:list2}
print(CTF4)
list2=tuple(list2)
CTF4={tup:list2}
print(CTF4)
tup=list(tup)
#CTF4={tup:list2}                   ##TypeError: unhashable type: 'list'

#字典内置方法
dict.clear(dict1)               #清空一个字典
print(dict1,len(dict1))
print('\n')

CTF=CTF1.copy()                 #返回一个字典的浅复制
print(CTF)
#直接赋值和 copy 的区别
dict1 = {'user': 'normal', 'num': [1, 2, 3]}
dict2 = dict1  # 浅拷贝: 引用对象
dict3 = dict1.copy()  # 浅拷贝：深拷贝父对象（一级目录），子对象（二级目录）不拷贝，子对象是引用
print(dict1)
print(dict2)
print(dict3)
# 修改 data 数据
dict1['user'] = 'root'
dict1['num'].remove(1)
# 输出结果
print(dict1)
print(dict2)
print(dict3)
# dict2 其实是 dict1 的引用（别名），所以输出结果都是一致的，dict3 父对象进行了深拷贝，不会随dict1 修改而修改，子对象是浅拷贝所以随 dict1 的修改而修改
#https://www.runoob.com/w3cnote/python-understanding-dict-copy-shallow-or-deep.html
print('\n')

#字典 fromkeys() 函数用于创建一个新字典，以序列 seq 中元素做字典的键，value 为字典所有键对应的初始值,默认为 none
CTF3=dict.fromkeys(list1,'CFT program')
print(CTF3)
print('\n')

#字典 get() 函数返回指定键的值
print(CTF1.get('web','Invalid Data'))
print(CTF1.get('ICT','Invalid Data'))
#get() 方法 和 dict[key] 访问元素区别
#get(key) 方法在 key（键）不在字典中时，可以返回默认值 None 或者设置的默认值。
#dict[key] 在 key（键）不在字典中时，会触发 KeyError 异常
print(emptyDict1.get('key','Invalid Data'))
#print(emptyDict1['key'])       ##KeyError: 'key'
#get() 方法对嵌套字典的使用方法
index={'Benjamin_C':{'url':'benjamin101v.github.io'}}
res=index.get('Benjamin_C',{}).get('url')
print(res)
print('\n')

#字典 in 操作符用于判断键是否存在于字典中，如果键在字典 dict 里返回 true，否则返回 false；not in 反之
print('web' in CTF1)
print('网络安全' in CTF1)
print('\n')

#字典视图对象（view objects）
#视图对象字典实体的动态视图，这就意味着字典改变，视图也会跟着变化
#items() 方法以列表返回视图对象，是一个可遍历的key/value 对
print(CTF1.items())
for key,value in CTF1.items():
    print(f'{key}:{value}')
#keys()
print(CTF1.keys())
#values()
print(CTF1.values())
print('\n')

#字典 setdefault() 方法和 get()方法 类似, 如果键不存在于字典中，将会添加键并将值设为默认值
print(CTF1)
print(CTF1.setdefault('web','none'))
print(CTF1)
print(CTF1.setdefault('AI','none'))
print(CTF1)
print('\n')
#del CTF1['AI']

#dict.update(dict2)把字典参数 dict2 的 key/value(键/值) 对更新到字典 dict 里
print(CTF1)
replenish={'AI':'人工智能安全','blockchain':'区块链安全'}
CTF1.update(replenish)      #原有值会被新值所覆盖
print(CTF1)
print('\n')

#字典 pop() 方法删除字典 key（键）所对应的值，返回被删除的值
#如果 key 存在 - 删除字典中对应的元素
#如果 key 不存在 - 返回设置指定的默认值 default
#如果 key 不存在且默认值 default 没有指定 - 触发 KeyError 异常
print(CTF2)
print(CTF2.pop('reverse'))
print(CTF2)
print(CTF2.pop('AI','Invalid Data'))
#print(CTF2.pop('AI'))               ##KeyError: 'AI'

#字典 popitem() 方法随机返回并删除字典中的最后一对键和值
#如果字典已经为空，却调用了此方法，就报出 KeyError 异常
print(CTF3)
print(CTF3.popitem())
print(CTF3)
CTF3['AI']='人工智能安全'
print(CTF3)
print(CTF3.popitem())
print(CTF3)
#print(emptyDict1.popitem())         ##KeyError: 'popitem(): dictionary is empty'