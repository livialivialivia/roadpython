#! /usr/bin/env python
# _*_ coding: utf-8 _*_


def breakone():
    for i in range(5):
        if i == 2:
            break
        print i


def continueone():
    for i in range(5):
        if i == 2:
            continue
        print i


breakone()
#结果为:[0,1]
print '--------------'
continueone()
# 结果为[0,1,3,4,5]