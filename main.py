import numpy
import matplotlib.pyplot as plt
import csv
from sympy import *
import numpy as np
from scipy.optimize import minimize

x = Symbol('x')
y = Symbol('y')
xlist = list()
ylist = list()
reader = csv.DictReader(open("data-10.csv"), delimiter=',')
for line in reader:
    xlist.append(float(line["x"])) 
    ylist.append(float(line["y"]))
 
def f_x_2(x, c1, c2, c3, c4, c5):
    return c1*x + c2
    
def f_x_3(x, c1, c2, c3, c4, c5):
    return c1 + c2*x + c3*x*x 

def f_x_4(x, c1, c2, c3, c4, c5):
    return c1 + c2*x + c3*x*x + c4*ln(x)

def f_x_5(x, c1, c2, c3, c4, c5):
    return c1 + c2*x +c3*x*x + c5*sin(c4*x)

def f_x_10(x, c1, c2, c3, c4, c5):
    return c1 + c2*ln(x) +c3*x*x*x + c5*sin(c4*x)

def funToMinimize(c):
    res = 0
    n= min(len(xlist), len(ylist))
    for i in range(n):
        res = res + (ylist[i] - func(xlist[i], c[0], c[1], c[2], c[3], c[4]))**2
    return res

def Linear_MNK(x ,y):
    n = len(x)
    sum_x = 0
    sum_y = 0
    sum_xy = 0
    sum_x_2 = 0
    meas_error =0
    for i in range(0, n):
        sum_x = sum_x + x[i]
        sum_y = sum_y + y[i]
        sum_xy = sum_xy + x[i]*y[i]
        sum_x_2 = sum_x_2 + x[i]*x[i]
    
    a = (n*sum_xy-sum_x*sum_y)/(n*sum_x_2 - sum_x*sum_x)
    b = (sum_y - a*sum_x)/n
    for i in range(0, n):
        meas_error = meas_error + (y[i] - get_y(x[i], a, b))**2
    print("Measurement error is", meas_error)
    print(sum_x, sum_y, sum_xy, sum_x_2, n)
    print(a, "x+", b)

def print_plot(x, y, c):
    n=min(len(x), len(y))
    plt.plot(xlist , ylist, linestyle=":", marker="x", color='green', linewidth =2 , label='табличні дані')
    x1list = list()
    y1list = list()
    for i in range(n):
        x1list.append(x[i])
        y1list.append(f_x_10(x[i], c[0], c[1], c[2], c[3], c[4]))
    plt.plot (x1list, y1list)
    plt.show()
#Linear_MNK()

c = [1., 1., 1., 1., 1., 1.]
#c = [0., 0., 0., 0., 0., 0.]
print(c)
minimizedFun = minimize(funToMinimize, c)
print(minimizedFun.x)
print("raznica ", funToMinimize(minimizedFun.x))
print_plot(xlist, ylist, minimizedFun.x)
#Linear_MNK(xlist1, ylist1)      