# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 14:23:23 2021

@author: raj patil
"""
for i in range(int(input())):
    
    
    w1,w2,x1,x2,m = map(int,input().split())

    mini = w1 + (x1 * m)
    maxi = w1 + (x2 * m)

    if mini <= w2 and w2 <= maxi:
        print("1")
    else:
        print("0")
    
    
    
    
    