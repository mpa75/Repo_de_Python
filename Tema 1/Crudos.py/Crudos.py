# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 12:32:55 2022

@author: Fran
"""

import numpy as np
from scipy.optimize import minimize
from numpy.random import random

f=lambda x: 6*x[0]+16*x[1]+10*x[2]-9*x[7]-15*x[8]
rest=({'type':'ineq', 'fun': lambda x: x[0]*x[5]+3*x[1]*x[3]+x[1]*x[5]-x[0]*x[3]},
      {'type':'ineq', 'fun': lambda x: x[1]*x[4]-3*x[0]*x[4]-x[0]*x[6]-x[1]*x[6]},
      {'type':'eq', 'fun': lambda x: x[0]+x[1]-x[3]-x[4]},
      {'type':'eq', 'fun': lambda x: x[2]-x[5]-x[6]},
      {'type':'eq', 'fun': lambda x: x[3]+x[5]-x[7]},
      {'type':'eq', 'fun': lambda x: x[4]+x[6]-x[8]})

cotas=((0,None),(0,None),(0,None),(0,None),(0,None),(0,None),(0,None),(0,100),(0,200))
seed1=np.ones(9)*10
seed2=[10,0,10,40,0,50,50,60,0]
seed3=[10,0,10,40,0,50,50,60,10]
res=minimize(f,seed1,bounds=cotas,constraints=rest)
print(res.x.round(1), np.round(res.fun))  


# for k in range(10**5):
#     x=random(9)*200
#     x[4]=x[0]+x[1]-x[3]
#     x[6]=x[2]-x[5]
#     x[7]=x[3]-x[5]
#     x[8]=x[4]+x[6]
#     if (x>=0).all() and x[7]<=100 and rest[0].get('fun')(x)>=0 and rest[1].get('fun')(x)>=0:
#         if f(x)<-1000:
#             print (x,f(x))
