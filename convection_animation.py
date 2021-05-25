import matplotlib.pyplot as plt
import numpy as np
from math import *
from functools import cache
from matplotlib import cm
from mpl_toolkits.mplot3d import axes3d
from matplotlib import style

style.use('dark_background')

n = 200
T = 300000
tmax = 1000
D = 0.0001
theta = 20
vx = 1

x = np.linspace(-8, 8, n)
y = np.linspace(-8, 8, n)

X, Y = np.meshgrid(x, y)

t = np.linspace(0, tmax, T)

dx = x[1]-x[0]
dy = y[1]-y[0]
dt = t[1]-t[0]

def psi_0(x, y):
    T = theta*((np.exp(-0.2*(x-2)**2)+np.exp(-0.2*(x+2)**2)) * np.exp(-0.1*y**2))
    return(T)

def v(x):
    Vx = []
    for j in range(n):
        S = -vx*np.exp(-0.2*(x[j]-6.7)**2)
        Vx.append(S)
    return(Vx)

Vx = v(x)

def temperature():
    Temperature_ = []
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
                xw = Temp[i-1][j][w] + (((D*(((Temp[i-1][j][w+2]- 2*Temp[i-1][j][w+1] + Temp[i-1][j][w])/(dx*dx)) + ((Temp[i-1][j+2][w] - 2*Temp[i-1][j+1][w] + Temp[i-1][j][w])/(dy*dy)))) - (Vx[w]*(Temp[i-1][j+1][w] - Temp[i-1][j][w])/dy)) * dt)
                Xw.append(xw)
                if x[w] == x[int(n/2)+int((n/20)*2.2)]:
                    if y[j] == y[int(n/2)]:
                        Temperature_.append(xw)
                        if xw < (theta/2):
                            print(xw)
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
        print(i, "/", T, ", // temperature = ", Temperature_[i-2])
    return(Temp)

Temp = temperature()

plt.imshow(psi_0(X, Y))
plt.show()

fig = plt.figure()
ax1 = plt.subplot(projection= '3d')
i = 0
while 1000*i < T:
    ax1.clear()
    ax1.plot_surface(X, Y, Temp[1000*i], cmap = cm.plasma, linewidth=0, alpha = 1, antialiased=True)
    ax1.axes.set_xlim3d(left=-10, right=10)
    ax1.axes.set_ylim3d(bottom=-10, top=10)
    ax1.axes.set_zlim3d(bottom=0, top= theta + theta/10)
    ax1.set_title(i)
    plt.savefig("{}".format(i))
    plt.pause(0.000001)
    i = i + 1
