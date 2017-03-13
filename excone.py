#! /usr/bin/env python
# _*_ coding: utf-8 _*_
import math


#练习一：for嵌套for循环输出10-50中个位带有1到5的所有数字
def practiseone():
    for i in range(10, 50):
        if i % 10 in [ 1, 2, 3, 4, 5 ]:
            print i,
#此处有个小知识点即print打印后面加上逗号,就不会换行。
print 'practise one~~~~~~~~~~~~~~'
practiseone()


#练习二: 执行指定次数循环
def practisetwo():
    a = 0
    while a<4:
        print a,
        a += 1
print '\n'
print 'practise two~~~~~~~~~~~~~~'
practisetwo()

#练习三：遍历字母和列表
def practisethree():
    a = 'qwerqwelasdfasdfasd'
    for i in a:
        print i,
    b = [3,4,5,6,7,8,9]
    for i in b:
        print i,
print '\n'
print 'practise three~~~~~~~~~~~~~~'
practisethree()

#练习四：通过序列索引迭代
def practisefour():
    a = 'testlearning'
    for i in range(len(a)):
        print a[i],
print '\n'
print 'practise four~~~~~~~~~~~~~~'
practisefour()

#练习五：判断是否为素数(不能被1和该数的开方之间的所有数整除)
def number_judge():
    try:
        input_number = int(raw_input("Please input a number: "))
        data = (math.sqrt(input_number))+1
        for i in range(2, int(data)):
            if input_number % i == 0:
            return False
        return True
    except Exception, e:
        print u'输入有误，不是数字！'

def practisefive():
    result = number_judge()
    if result:
        print u'是素数！'
    else:
        print u'不是素数！'

print '\n'
print 'practise five~~~~~~~~~~~~~~'
practisefive()