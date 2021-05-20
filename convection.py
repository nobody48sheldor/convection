import matplotlib.pyplot as plt
import numpy as np
from math import *
from functools import cache
from matplotlib import cm
from mpl_toolkits.mplot3d import axes3d
from matplotlib import style

style.use('dark_background')

n = 150
T = 150
tmax = 10
D = 0.04
theta = 15
vx = np.linspace(0, 100, T)

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

def v(x):
    Vx = []
    for i in range(n):
        V = []
        for j in range(n):
            S = -vx[i]*np.exp(-1.5*(x[j]-5.8)**2)
            V.append(S)
        Vx.append(V)
    return(Vx)

Vx = v(x)
print(len(Vx), len(Vx[0]))

def temperature_temps():
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
                xw = Temp[i-1][j][w] + ((D*((Temp[i-1][j][w+2]- 2*Temp[i-1][j][w+1] + Temp[i-1][j][w])/(dx**2) + (Temp[i-1][j+2][w] - 2*Temp[i-1][j+1][w] + Temp[i-1][j][w])/(dy**2))) - (V[w]*(Temp[i-1][j+1][w] - Temp[i-1][j][w])/dy)) * dt
                Xw.append(xw)
                if x[w] == x[int(n/2)+int((n/20)*2.2)]:
                    if y[j] == y[int(n/2)]:
                        Temperature_.append(xw)
                        if xw < theta/20:
                            return(i*dt)
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

Temps = []
TEMP = 0
i = 0
while i < n:
    V = Vx[i]
    if temperature_temps() ==  None:
        TEMP = Temps[i-1]
    if type(temperature_temps()) == float:
        TEMP = 1/temperature_temps()
    print("TEMP = ", TEMP)
    Temps.append(TEMP)
    print(i)
    i = i + 1
print(len(Temps))


plt.imshow(psi_0(X, Y))
plt.show()

plt.plot(vx, Temps)
plt.show()
