import numpy
import matplotlib.pyplot as plt
import csv
from sympy import *
import numpy as np
from scipy.optimize import minimize


def f_x_2(x, c1, c2, c3, c4, c5):
    return c1*x + c2
 
def f_x_3(x, c1, c2, c3, c4, c5):
    return c1 + c2*x + c3*x*x

def f_x_4(x, c1, c2, c3, c4, c5):
    return c1 + c2*x + c3*x*x + c4*ln(x)

def f_x_5(x, c1, c2, c3, c4, c5):
    return c1 + c2*x +c3*x*x + c5*sin(c4*x)

def f_x_10(x, c1, c2, c3, c4, c5):
    return c1*x + c2*sinh(x) + c3*atan(x) + c4*tanh(x)

x = Symbol('x')
y = Symbol('y')
xlist = list()
ylist = list()
datalist = ["data-2.csv", "data-3.csv","data-4.csv","data-5.csv", "data-10.csv"]
funclist = [f_x_2, f_x_3, f_x_4, f_x_5, f_x_10]

reader = csv.DictReader(open("data-10.csv"), delimiter=',')
for line in reader:
    xlist.append(float(line["x"])) 
    ylist.append(float(line["y"]))
 

def funToMinimize(c):
    res = 0
    n= min(len(xlist), len(ylist))
    for i in range(n):
        res = res + (ylist[i] - f_x_10(xlist[i], c[0], c[1], c[2], c[3], c[4]))**2
    return res

def funToMinimize1(c, func, x1, y1):
    res = 0
    n= min(len(x1), len(y1))
    for i in range(n):
        res = res + (y1[i] - func(x1[i], c[0], c[1], c[2], c[3], c[4]))**2
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

def print_plot1(c, func, data):
    reader = csv.DictReader(open(data), delimiter=',')
    x1list = list()
    y1list = list()
    x2list = list()
    y2list = list()
    for line in reader:
        x1list.append(float(line["x"])) 
        y1list.append(float(line["y"]))
    n=min(len(x1list ), len(y1list ))
    plt.plot(x1list , y1list, linestyle=":", marker="x", color='green', linewidth =2 , label='табличні дані')
    for i in range(n):
        x2list.append(x1list[i])
        y2list.append(func(x1list[i], c[0], c[1], c[2], c[3], c[4]))
    plt.plot (x2list, y2list)
    print(i, ") ", "Measurement error is ", funToMinimize1(c, func, x1list, y1list))
    plt.show()

c = [1., 1., 1., 1., 1., 1.]
#c = [0., 0., 0., 0., 0., 0.]

c2  = [3.00846915,   0.0115911,        1.,         1.,          1.,         1.        ]
c3  = [-0.162471,    3.75442129,     -0.87552091,  1.,          1.,         1.        ]
c4  = [0.41721302,   2.08172032, -0.76707734 , 5.46468578,      1.,         1.        ]
c5  = [ 0.06209793,  5.12100163,  1.91624632 , 4.11536373,    -2.0474313,   1.        ]
c10 = [4.5685805197072636E+02, -2.6438686779740692E+01, -2.4696375471488686E+03, 2.0217128471789802E+03, 1., 1.]
clist = [c2,c3,c4,c5,c10]

print(c)
#minimizedFun = minimize(funToMinimize, c)
for i in range(5):
    print_plot1(clist[i], funclist[i], datalist[i])
    
#print_plot1(c10, f_x_10, "data-10.csv")
#print_plot(xlist, ylist, c, f_x_2)
#print(minimizedFun.x)
#print("Measurement error is ", funToMinimize(minimizedFun.x))
#print_plot(xlist, ylist, minimizedFun.x)
#Linear_MNK(xlist1, ylist1)      
