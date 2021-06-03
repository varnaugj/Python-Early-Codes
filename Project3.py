#Import critical gui functions and libraries for math manipulation
import tkinter as tk
from tkinter import *
from tkinter import ttk
import numpy as np
import matplotlib.pyplot as plt
from scipy import random


a = 0
b = np.pi
c = 0
d = np.pi
e = 0
g = np.pi
N = 1000

def f(x):
    return np.sin(x)

def Integrate_Run(list,number):
    plt.figure(1)
    plt.subplot(311)
    for i in range (int(number)):
        ar = np.zeros(N)

        for i in range(len(ar)):
            ar[i] = random.uniform(a,b)

        integral = 0.0

        for i in ar:
            integral += f(i)

        ans = (b-a)/float(N)*integral
        #print("The value calculated by monte carlo integration is ",format(ans))
        list.append(ans)
    plt.title("Monte Carlo Distribution values 1D Integral")
    plt.hist(list, bins = 30, ec="black")
    plt.pause(0.05)
    #print(list)


def f2(x,y):
    return np.sin(x*y)

def DIntegrate_Run(list1,number):
    plt.subplot(312)
    plt.xlabel("Areas")
    plt.title("Monte Carlo Distribution values 2D Integral")
    for i in range (int(number)):
        arx = np.zeros(N)
        ary = np.zeros(N)
        

        for i in range(len(arx)):
            arx[i] = random.uniform(a,b)
        for i in range(len(ary)):
            ary[i] = random.uniform(c,d)
        
        IntegralFy = 0.0
        
        for i in range(len(arx)):
                IntegralFy += f2(arx[i],ary[i])
        Area = (b-a)*(d-c)
        final = (Area/float(N))*IntegralFy
        list1.append(final)
        #print(list)
    
    plt.hist(list1, bins = 30, ec="black")



def f3(x,y,z):
    q = x**2 + y**2 + z**2
    return q

def TIntegrate_Run(list2,number):
    plt.subplot(313)
    plt.xlabel("Areas")
    plt.title("Monte Carlo Distribution values 3D Integral")
    for i in range (int(number)):
        arx = np.zeros(N)
        ary = np.zeros(N)
        arz = np.zeros(N)
        

        for i in range(len(arx)):
            arx[i] = random.uniform(a,b)
        for i in range(len(ary)):
            ary[i] = random.uniform(c,d)
        for i in range(len(arz)):
            arz[i] = random.uniform(e,g)

        IntegralF3 = 0.0
        
        for i in range(len(arx)):
                IntegralF3 += f3(arx[i],ary[i],arz[i])
        Area = (b-a)*(d-c)*(g-e)
        final = (Area/float(N))*IntegralF3
        list2.append(final)
        #print(list)
    
    plt.hist(list2, bins = 30, ec="black")
    plt.draw()
    plt.tight_layout()
    plt.show()


Ans_list = []
Anslist = []
Ans_list3 = []
Integrate_Run(Ans_list,1000)
DIntegrate_Run(Anslist,1000)
TIntegrate_Run(Ans_list3,1000)



