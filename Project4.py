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
N = 1000

def f2(x,y):
    return np.sin(x*y)

def DIntegrate_Run(list1,number):
    plt.figure(1)
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
    plt.draw()
    plt.tight_layout()
    plt.show()

Anslist = []
DIntegrate_Run(Anslist,1000)