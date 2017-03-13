#! /usr/bin/env python
# _*_ coding: utf-8 _*_

#各层都用break，即层层break实现退出循环

def test():
    for i in range(2):
        for j in range(2):
            for k in range(2):
                if i == j ==k ==1:
                    break
                else:
                    print "i = %s,j = %s,k = %s" % (i, j, k)
            else:continue
            break
        else:continue
        break
test()
