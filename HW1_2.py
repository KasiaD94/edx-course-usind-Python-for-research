# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 13:54:32 2020

@author: Kasia
"""
import math
import random

def rand():
   return (random.uniform(-1,1))
   
def distance(x, y):
    a = abs(y[0]-x[0])
    b = abs(y[1]-x[1])
    c = math.sqrt(a*a + b*b)
    return c

def in_circle(point, origin = [0,0]):
   if distance(point, origin) < 1:
       return True
   else:
       return False

#random.seed(1) 
R = 10000
inside = []
count = 0
for i in range(R):
    point = (rand(), rand())
    inside.append (in_circle(point))
    if in_circle(point) == True:
        count += 1
        
proportion = count / R
print(proportion)