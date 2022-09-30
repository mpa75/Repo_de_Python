# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 12:32:55 2020

@author: Fran
"""

import numpy as np
from scipy.optimize import minimize
from numpy.random import random, seed

# seed(18)

c=np.array([200.,30.,200.,60.,50.,100.,50.])
f=lambda x: c@x
a=np.array([100.,20.,150.,50.,50.,150.,150.])
rest=({'type':'ineq', 'fun': lambda x: 500.-a@x},
      {'type':'eq', 'fun': lambda x: x[0]*(1-x[0])},
      {'type':'eq', 'fun': lambda x: x[1]*(1-x[1])},
      {'type':'eq', 'fun': lambda x: x[2]*(1-x[2])},
      {'type':'eq', 'fun': lambda x: x[3]*(1-x[3])},
      {'type':'eq', 'fun': lambda x: x[4]*(1-x[4])},
      {'type':'eq', 'fun': lambda x: x[5]*(1-x[5])},
      {'type':'eq', 'fun': lambda x: x[6]*(1-x[6])})


cotas=((0.,1.),(0.,1.),(0.,1.),(0.,1.),(0.,1.),(0.,1.),(0.,1.))
sem=random(7)
res=minimize(f,sem,bounds=cotas,constraints=rest)
continua=True
i=0
while continua:
    sem=random(7)
    res=minimize(f,sem,bounds=cotas,constraints=rest)
    if res.fun>600:
        continua=False
    i+=1
print(i)
print(res.x.round(1), np.round(res.fun),a@res.x)  
# #
# #


# M=0
# xM=np.zeros(7)
# for i in range(2**7):
#     binario=np.binary_repr(i,width=7)
#     x=np.array([int(d) for d in binario])
#     if a@x<=500 and c@x>M:
#         xM=x.copy()
#         M=c@x
# print(xM)
# print(M)