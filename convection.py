import matplotlib.pyplot as plt
import numpy as np
from math import *
from functools import cache
from matplotlib import cm
from mpl_toolkits.mplot3d import axes3d
from matplotlib import style
from concurrent.futures import ProcessPoolExecutor


style.use('dark_background')

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

def temperature_temps1(V1):
    Temperature_ = []
    Temp = []
    Yj = []
    Xw = []
    Temp.append(np.array(psi_0(X, Y)))
    i = 1
    while i < int(T/4):
        j = 0
        Yj = []
        while j < n-2:
            w = 0
            Xw = []
            while w < n-2:
                xw = Temp[i-1][j][w] + ((D*((Temp[i-1][j][w+2]- 2*Temp[i-1][j][w+1] + Temp[i-1][j][w])/(dx**2) + (Temp[i-1][j+2][w] - 2*Temp[i-1][j+1][w] + Temp[i-1][j][w])/(dy**2))) - (V1[w]*(Temp[i-1][j+1][w] - Temp[i-1][j][w])/dy)) * dt
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
#        print(i, "/", T)

def temperature_temps2(V2):
    Temperature_ = []
    Temp = []
    Yj = []
    Xw = []
    Temp.append(np.array(psi_0(X, Y)))
    i = int(T/4)
    while i < int(T/2):
        j = 0
        Yj = []
        while j < n-2:
            w = 0
            Xw = []
            while w < n-2:
                xw = Temp[i-1][j][w] + ((D*((Temp[i-1][j][w+2]- 2*Temp[i-1][j][w+1] + Temp[i-1][j][w])/(dx**2) + (Temp[i-1][j+2][w] - 2*Temp[i-1][j+1][w] + Temp[i-1][j][w])/(dy**2))) - (V2[w]*(Temp[i-1][j+1][w] - Temp[i-1][j][w])/dy)) * dt
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
#        print(i, "/", T)

def temperature_temps3(V3):
    Temperature_ = []
    Temp = []
    Yj = []
    Xw = []
    Temp.append(np.array(psi_0(X, Y)))
    i = int(T/2)
    while i < int(3*T/4):
        j = 0
        Yj = []
        while j < n-2:
            w = 0
            Xw = []
            while w < n-2:
                xw = Temp[i-1][j][w] + ((D*((Temp[i-1][j][w+2]- 2*Temp[i-1][j][w+1] + Temp[i-1][j][w])/(dx**2) + (Temp[i-1][j+2][w] - 2*Temp[i-1][j+1][w] + Temp[i-1][j][w])/(dy**2))) - (V3[w]*(Temp[i-1][j+1][w] - Temp[i-1][j][w])/dy)) * dt
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
#        print(i, "/", T)

def temperature_temps4(V4):
    Temperature_ = []
    Temp = []
    Yj = []
    Xw = []
    Temp.append(np.array(psi_0(X, Y)))
    i = int(3*T/4)
    while i < T:
        j = 0
        Yj = []
        while j < n-2:
            w = 0
            Xw = []
            while w < n-2:
                xw = Temp[i-1][j][w] + ((D*((Temp[i-1][j][w+2]- 2*Temp[i-1][j][w+1] + Temp[i-1][j][w])/(dx**2) + (Temp[i-1][j+2][w] - 2*Temp[i-1][j+1][w] + Temp[i-1][j][w])/(dy**2))) - (V4[w]*(Temp[i-1][j+1][w] - Temp[i-1][j][w])/dy)) * dt
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
#        print(i, "/", T)

def func1():
    Temps1 = []
    TEMP1 = 0
    V1 = []
    i = 0
    while i < n:
        V1 = Vx[i]
        if temperature_temps1(V1) ==  None:
            TEMP1 = Temps1[i-1]
        else:
            TEMP1 = 1/temperature_temps1(V1)
        print("TEMP1 = ", TEMP1)
        Temps1.append(TEMP1)
        print(i)
        i = i + 1
    print(len(Temps1))
    return(Temps1)

def func2():
    Temps2 = []
    TEMP2 = 0
    V2 = []
    j = 0
    while j < n:
        V2 = Vx[j]
        if temperature_temps2(V2) ==  None:
            TEMP2 = Temps2[j-1]
        else:
            TEMP2 = 1/temperature_temps2(V2)
        print("TEMP2 = ", TEMP2)
        Temps2.append(TEMP2)
        print(j)
        j = j + 1
    print(len(Temps2))
    return(Temps2)

def func3():
    Temps3 = []
    TEMP3 = 0
    V3 = []
    w = 0
    while w < n:
        V3 = Vx[w]
        if temperature_temps3(V3) ==  None:
            TEMP3 = Temps3[w-1]
        else:
            TEMP3 = 1/temperature_temps3(V3)
        print("TEMP3 = ", TEMP3)
        Temps3.append(TEMP3)
        print(w)
        w = w + 1
    print(len(Temps3))
    return(Temps3)

def func4():
    Temps4 = []
    TEMP4 = 0
    V4 = []
    h = 0
    while h < n:
        V4 = Vx[h]
        if temperature_temps4(V4) ==  None:
            TEMP4 = Temps[h-1]
        else:
            TEMP4 = 1/temperature_temps4(V4)
        print("TEMP4 = ", TEMP4)
        Temps4.append(TEMP4)
        print(h)
        h = h + 1
    print(len(Temps4))
    return(Temps4)

n = 150
T = 50
tmax = 100
D = 0.06
theta = 15
vx = np.linspace(0, 100, n)

x = np.linspace(-10, 10, n)
y = np.linspace(-10, 10, n)

X, Y = np.meshgrid(x, y)

t = np.linspace(0, tmax, T)

dx = x[1]-x[0]
dy = y[1]-y[0]
dt = t[1]-t[0]

Vx = v(x)
print(len(Vx), len(Vx[0]))

def main():
    executor = ProcessPoolExecutor(max_workers=10)
    P1 = executor.submit(func1)
    P2 = executor.submit(func2)
    P3 = executor.submit(func3)
    P4 = executor.submit(func4)

    T1 = P1.result()
    T2 = P2.result()
    T3 = P3.result()
    T4 = P4.result()

    Temps = []
    for i in range(T1-1):
        Temps.append(T1[i])
    for i in range(T2-1):
        Temps.append(T2[i])
    for i in range(T3-1):
        Temps.append(T3[i])
    for i in range(T4-1):
        Temps.append(T4[i])

    plt.imshow(psi_0(X, Y))
    plt.show()

    plt.plot(vx, Temps)
    plt.show()
