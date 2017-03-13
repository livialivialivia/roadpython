#! /usr/bin/env python
# _*_ coding: utf-8 _*_

#打印二维数组4*4

import random

def print_array():
    for i in range(4):
        for j in range(4):
            print "%6s" %random.randint(1,20),
        print

print_array()

# 格式化打印"%6s",即每个元素占6个位置