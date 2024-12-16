set1={'web','misc','crypto','pwn','reverse','AI','blockchain'}
list1=['web','misc','crypto','pwn','reverse']
set2=set(list1)
emptySet=set()
print(type(set1),set1)
print(type(set2),set2)
print(type(emptySet),emptySet)
print('\n')

#集合运算
print('web' in set1)        #查找
print('AI' in set2)

print(set1-set2)            #差集，集合 set1 中包含而集合 set2 中不包含的元素
print(set2-set1)            #集合 set2 中包含而集合 set1 中不包含的元素

print(set1 | set2)          #并集

print(set1 & set2)          #交集

print(set1 ^ set2)          #交集的补集
print('\n')

#集合的基本操作
#添加一个元素
set2.add('CTF')
print(set2)
new=set1-set2
#set2.add(new)          ##TypeError: unhashable type: 'set'
new=tuple(new)
set2.add(new)
print(set2)
#移除一个元素
print(set1)
set1.remove('blockchain')
set1.discard('AI')
#set1.remove('AI')           ##KeyError: 'AI'
set1.discard('blockchain')   #discard 方法在指定元素不存在时不会发生错误
print(set1)
#添加多个元素（参数为列表，元组，字典等）
print(set1)
set1.update(['AI','blockchain'])
print(set1)
#集合的 pop 方法会对集合进行无序的排列，然后将这个无序排列集合的左面第一个元素进行删除
print(set1)
print(set1.pop())       #每次输出的结果不同
print(set1)
print('\n')

#其他集合内置方法
print(set2)
set2.clear()        #clear() 方法用于移除集合中的所有元素
print(set2)
print('\n')

print(set1)
set2=set1.copy()    #copy() 方法用于拷贝一个集合
print(set2)
print('\n')

set3={'web','misc','crypto','pwn','reverse','AI','blockchain'}
set4={'web','misc','crypto','pwn','reverse'}
print(set3.difference(set4))            #difference() 方法用于返回集合的差集，即返回的集合元素包含在第一个集合中，但不包含在第二个集合(方法的参数)中
print(set4.difference(set3))
print('\n')

set3.difference_update(set4)     #difference_update() 方法用于移除两个集合中都存在的元素
print(set3)     #difference_update() 方法与 difference() 方法的区别在于 difference() 方法返回一个移除相同元素的新集合，而 difference_update() 方法是直接在原来的集合中移除元素，没有返回值
print(set4)
print('\n')

set5={'web','misc','crypto','pwn','reverse','AI','blockchain'}
set6={'web','misc','crypto','pwn','reverse'}
print(set1)
print(set5.intersection(set6))      #intersection() 方法用于返回两个或更多集合中都包含的元素，即交集
print(set5.intersection(set6,set1))
print('\n')

print(set2)
set5.intersection_update(set6)
print(set5)
print(set6)
set5.intersection_update(set1,set2)
print(set5)
print('\n')

#更多方法参见https://www.runoob.com/python3/python3-set.html