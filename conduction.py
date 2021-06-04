import matplotlib.pyplot as plt
import numpy as np
from math import *
from functools import cache
from matplotlib import cm
from mpl_toolkits.mplot3d import axes3d
from matplotlib import style

style.use('dark_background')

n = int(input("n = "))
T = int(input("T = "))
tmax = float(input("tmax = "))
D = float(input("D = "))
theta = float(input("theta = "))


x = np.linspace(-10, 10, n)
y = np.linspace(-10, 10, n)

X, Y = np.meshgrid(x, y)

t = np.linspace(0, tmax, T)

dx = x[1]-x[0]
dy = y[1]-y[0]
dt = t[1]-t[0]

def psi_0(x, y):
    T = theta*((np.exp(-0.2*(x-2)**2)+np.exp(-0.2*(x+2)**2)) * np.exp(-0.1*y**2))
    return(T)
Temperature_ = []

def tempertature():
    Temp = []
    Yj = []
    Xw = []
    Temp.append(np.array(psi_0(X, Y)))
    i = 1
    while i < T:
        j = 0
        Yj = []
        while j < n-2:
            w = 0
            Xw = []
            while w < n-2:
                if i > 10:
                    if ((Temp[i-1][j][w] - Temp[i-10][j][w])/dt) > theta*5000/T:
                        xw = Temp[i-9][j][w]
                    else:
                        xw = Temp[i-1][j][w] + ((D*(((Temp[i-1][j][w+2]- 2*Temp[i-1][j][w+1] + Temp[i-1][j][w])/(dx*dx)) + ((Temp[i-1][j+2][w] - 2*Temp[i-1][j+1][w] + Temp[i-1][j][w])/(dy*dy)))) * dt)
                else:
                    xw = Temp[i-1][j][w] + ((D*(((Temp[i-1][j][w+2]- 2*Temp[i-1][j][w+1] + Temp[i-1][j][w])/(dx*dx)) + ((Temp[i-1][j+2][w] - 2*Temp[i-1][j+1][w] + Temp[i-1][j][w])/(dy*dy)))) * dt)
                Xw.append(xw)
                if x[w] == x[0]:
                    if y[j] == y[0]:
                        Temperature_.append(xw)
                w = w + 1
            Xw.append(xw)
            Xw.append(xw)
            Yj.append(Xw)
            j = j + 1
        Yj.append(Xw)
        Yj.append(Xw)
        Yja = np.array(Yj)
        Temp.append(Yja)
        i = i + 1
        print(i, "/", T)
    return(Temp)

Temp = tempertature()

plt.imshow(psi_0(X, Y))
plt.show()
Temperature_.append(Temperature_[T-2])

plt.plot(t, Temperature_)
plt.show()

input("//")

plt.ion()

fig = plt.figure()
ax1 = plt.subplot(projection = '3d')

i = 0
while i < T:
    ax1.clear()
    ax1.plot_surface(X, Y, Temp[i], cmap = cm.plasma, linewidth=0, alpha = 1, antialiased=True)
    ax1.axes.set_xlim3d(left=-10, right=10)
    ax1.axes.set_ylim3d(bottom=-10, top=10)
    ax1.axes.set_zlim3d(bottom=0, top= theta + theta/20)
    ax1.set_title(i)
    plt.pause(0.0001)
    i = i + 1
