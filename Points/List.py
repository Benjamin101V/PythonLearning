list1=['VIRTUAL','GUARD','Security']
print('list1:{}'.format(list1))
print('list1:',list1)
print('list1[1:3]:',list1[1:3])

#更新列表
list1.append('CTF')
list1.append(101)
print('list1:{}'.format(list1))

#删除列表元素
del list1[3]
print('list1:{}'.format(list1))

#列表脚本操作符
print('length of list1:',len(list1))                    #长度
print(list1+['web','misc','crypto','reserve','pwn'])    #组合
print(list1*2)                                          #重复
print('CTF' in list1)                                   #查找
for i in list1:                                         #迭代
    print(i)

#列表截取
print(list1[2])
print(list1[-2])
print(list1[1:])
print(list1[:3])

#列表函数
list2=['web','misc','crypto','reserve','pwn']

print('length of list2:',len(list2))    #计算元素个数

print(max(list2))                       #返回列表元素的最大值

print(min(list2))                       #最小值

tup=('web','misc','crypto','reserve','pwn')
print(list(tup))                        #将元组转化为列表

#列表方法
list2.append('CTF')             #在列表末尾添加新的对象
print(list2)

print(list2.count('CTF'))       #统计某个元素在列表中出现的次数

print(list1)
list1.extend(list2)             #在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
print(list1)

print('101引索位置:',list1.index(101))      #index() 函数用于从列表中找出某个值第一个匹配项的索引位置，如果没有找到对象则抛出异常
print('web的引索位置:',list2.index('web',0,5))   #可选择查找的起始位置和结束位置

list1.insert(2,'Benjamin')  #insert() 函数用于将指定对象插入列表的指定位置
print(list1)

res=list1.pop()                    #pop() 函数用于移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
print(res)
print(list1)
print(list1.pop(2))                #打印返回值
print(list1)

list1.remove(101)                  #remove() 函数用于移除列表中某个值的第一个匹配项
print(list1)

list1.reverse()                    #reverse() 函数用于反向列表中元素
print(list1)

list1.sort()                       #sort() 函数用于对原列表进行排序，如果指定参数，则使用比较函数指定的比较函数
print(list1)
list1.sort(key=None,reverse=True)  #未指定 reverse 参数时默认按照 ASCII 升序排列，这里是降序
print(list1)
list1.sort(key=str.lower)          #不区分大小写
print(list1)

#使用 enumerate 函数将序列组合为一个引索序列
for index,item in enumerate(list2):
    print(index+1,item)