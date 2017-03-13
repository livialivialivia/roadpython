#! /usr/bin/env python
# _*_ coding: utf-8 _*_

def print_grade_level(grades):
    if 90 <= grades <= 100:
        print 'Excellent!'
    elif 80<= grades < 90:
        print 'Fine!'
    elif 60 <= grades < 80:
        print 'Just OK'
    else:
        print 'You\'re failure!'


while True:
    try:
        grades = float(raw_input('Plesase input your scoure:  '))
        print_grade_level(grades)
    except Exception,e:
        print 'Please input the invalid number!'

#没有加上float,造成输入任何正整数都是you're failure!
#重点:加上float