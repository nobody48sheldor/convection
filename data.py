import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np

style.use('dark_background')

tmax = 60

t_ = np.linspace(0, 100*tmax, 10000)

with open("data11.txt", "r") as DATA1:
    data1 = DATA1.read().splitlines()

DATA1 = []

for i in data1:
    a = float(i)
    DATA1.append(a)

with open("data22.txt", "r") as DATA2:
    data2 = DATA2.read().splitlines()

DATA2 = []

for i in data2:
    a = float(i)
    DATA2.append(a)

with open("data33.txt", "r") as DATA3:
    data3 = DATA3.read().splitlines()

DATA3 = []

for i in data3:
    a = float(i)
    DATA3.append(a)

with open("data.txt", "r") as DATA4:
    data4 = DATA4.read().splitlines()

DATA4 = []

for i in data4:
    a = float(i)
    DATA4.append(a)

t = np.linspace(0, tmax, len(DATA1))
dt = t[1]-t[0]

plt.plot(t, DATA1, color = 'blue', marker= 'x', label = "high wind (10 m/s)")
plt.plot(t, DATA3, color = 'yellow', marker= 'x', label = "low wind (3.5 m/s)")
plt.plot(t, DATA2, color = 'red', marker= 'x', label = "no wind (0 m/s)")
plt.legend()
plt.show()

def derivative(data):
    D = []
    for i in range(len(data)-1):
        D.append(((data[i+1]-data[i])/(dt*data[i])))
    D.append(D[len(D)-1])
    m = np.mean(D)
    s = np.std(D)
    print(m)
    print(s)
    return(D)

#plt.plot(t, DATA4, color = 'green', marker= 'x')

print("high wind")
plt.plot(t, derivative(DATA1))
print("low wind")
plt.plot(t, derivative(DATA3))
print("no wind")
plt.plot(t, derivative(DATA2))
plt.show()
