import numpy as np
import matplotlib.pyplot as plt

a = float(input("Enter alpha "))
b = float(input("Enter beta "))
c = float(input("Enter gamma "))
d = float(input("Enter delta "))

y = np.array([int(input("Enter number of rabbits ")), int(input("Enter number of foxes "))])

def f(t, y):
	return (np.array([a*y[0] - b*y[0]*y[1],-c*y[1]+d*y[0]*y[1]]))

t = 0

T = np.arange(100)
Y = np.zeros(100)
Y[0] = y[1]
X = np.zeros(100)
X[0] = y[0]

for i in range(1,100):

	k1 = f(i-1, [X[i-1],Y[i-1]])
	k2 = f(i-0.5, [X[i-1]+0.5*k1[0], Y[i-1]+0.5*k1[1]])
	k3 = f(i-0.5, [X[i-1]+0.5*k2[0], Y[i-1]+0.5*k2[1]])
	k4 = f(i, [X[i-1]+1*k3[0], Y[i-1]+k3[1]])
	X[i] = X[i-1] + (k1[0]+2*k2[0]+2*k3[0]+k4[0])/6
	Y[i] = Y[i-1] + (k1[1]+2*k2[1]+2*k3[1]+k4[1])/6

plt.plot(T, X, 'g', T, Y, 'r')
plt.show()