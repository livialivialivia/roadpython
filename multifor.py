#! /usr/bin/env python
# _*_ coding: utf-8 _*_


#try except+pass共用实现退出多重循环


class getoutofloop(Exception):
    pass

try:
    for i in range(2):
        for j in range(2):
            for k in range(2):
                if i == j == k == 1:
                    raise getoutofloop()
                else:
                    print "i = %s,j = %s,k = %s" %(i,j,k)
except getoutofloop:
    pass

