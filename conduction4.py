import matplotlib.pyplot as plt
import numpy as np
from math import *
from functools import cache
from matplotlib import cm
from mpl_toolkits.mplot3d import axes3d
from matplotlib import style

dx = 0.2
dy = 0.2
dt = 0.02

tmax = 20
D = 0.2
temp_0 = 20
wind_speed = 0

print(np.exp(-D*tmax))
r = dt/(dx*dx + dy*dy)

print(r)
if r > 1/2:
    print("ne converge pas")
else:
    print("converge")

x = np.linspace(-10, 10, int(20/dx))
y = np.linspace(-10, 10, int(20/dy))

X, Y = np.meshgrid(x, y)

t = np.linspace(0, tmax, int(tmax/dt))

def temperature_init(x, y):
    S = temp_0*(np.exp(-0.2*(x**2 + y**2)) - 0.6*np.exp(-4*((x-2)**2 + y**2)))
    return(S)

def wind(wind_speed, x):
    V = []
    v = 0
    while v < len(x):
        if x[v] < 5:
            V.append(0)
        if x[v] > 5:
            V.append((wind_speed*np.log(x[v]-4)))
        v = v + 1
    return(V)

Wind = wind(wind_speed, x)

plt.plot(x, Wind)
plt.show()

Temp_init = np.array(temperature_init(X, Y))
print(len(Temp_init))

def temperature():
    Temperature = []
    Temperature.append(np.array(Temp_init))
    i = 1
    while i < int(tmax/dt):
        Yj = []
        Yj.append(Temperature[i-1][0])
        j = 1
        while j < int(len(y)-1):
            Xw = []
            Xw.append(Temperature[i-1][j][0])
            w = 1
            while w < int(len(x)-1):
                xw = Temperature[i-1][w][j] + ( ((D * (((Temperature[i-1][j][w+1] - 2*Temperature[i-1][j][w] + Temperature[i-1][j][w-1]) / (dx*dx)) + ((Temperature[i-1][j+1][w] - 2*Temperature[i-1][j][w] + Temperature[i-1][j-1][w]) / (dy*dy)) ) ) - (Wind[w] * ((Temperature[i-1][j+1][w] - Temperature[i-1][j-1][w]) / (2*dy)) ) ) *dt)
                Xw.append(xw)
                w = w + 1
            Xw.append(Temperature[i-1][j][len(x)-1])
            Yj.append(Xw)
            j = j + 1
        Yj.append(Temperature[i-1][len(y)-1])
        Temperature.append(np.array(Yj))
        print(i, " / ", int(tmax/dt))
        i = i + 1
    return(Temperature)

Temp = temperature()

fig = plt.figure()
ax1 = plt.subplot(projection= '3d')
T = 0
while T < int(tmax/(dt*15)):
    ax1.clear()
    ax1.plot_surface(X, Y, Temp[T*15], cmap = cm.plasma, linewidth=0, alpha = 1, antialiased=True)
    ax1.axes.set_xlim3d(left=-10, right=10)
    ax1.axes.set_ylim3d(bottom=-10, top=10)
    ax1.axes.set_zlim3d(bottom=0, top= temp_0 + temp_0/20)
    ax1.set_title(T)
    plt.pause(0.000001)
    T = T + 1
