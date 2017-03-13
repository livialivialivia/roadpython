#! /usr/bin/env python
# _*_ coding: utf-8 _*_

# return实现退出多重循环

def test():
    for i in range(2):
        for j in range(2):
            for k in range(2):
                if i == j == k == 1:
                    return
                else:
                    print "i = %s,j = %s,k = %s" % (i, j, k)



test()
