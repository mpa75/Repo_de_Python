# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 12:19:53 2022

@author: fran
"""


## dataset https://www4.stat.ncsu.edu/~boos/var.select/diabetes.html

import csv
import numpy as np
from matplotlib import pyplot as plt
from scipy.optimize import linprog, minimize
from numpy.random import random

L=[]
with open('diabetes.txt', newline = '') as datos:                                                                                          
    	lee_datos = csv.reader(datos, delimiter='\t')
    	for linea in lee_datos:
    		L.append(linea)
            
m=len(L[1:])
print(L[0])
print(L[1])
D=np.array(L[1:],dtype='float64')[:m]

x=D[:,2]
y=D[:,-1]

plt.plot(x,y,'.',ms=5)
plt.xlabel('IMC')
plt.ylabel('glucosa en sangre')


f = lambda c: (abs(c[0]*x + c[1] - y)).sum() 
sol1_solver=minimize(f,[2,2]) # Falla, probablemente por no ser diferenciable la función objetivo
recta=lambda x: sol1_solver.x[0]*x+sol1_solver.x[1]
# plt.plot([19,41],[recta(15),recta(45)])

c=np.concatenate([np.ones(2*m),np.zeros(2)])
Aeq=np.concatenate([-np.eye(m),np.eye(m),np.array([x]).T,np.ones([m,1])],axis=1)
cotas=[(0,None)]*2*m
cotas.append((None,None))
cotas.append((None,None))

sol=linprog(c,A_eq=Aeq,b_eq=y,bounds=cotas)
plt.plot([19,41],[recta(15),recta(45)])

a=sol.x[-2]
b=sol.x[-1]

rec1=lambda x: a*x+b
plt.plot([19,41],[rec1(15),rec1(45)])



# plt.show()
# print(sol1_solver)

