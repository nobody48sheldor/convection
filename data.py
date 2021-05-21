import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np

style.use('dark_background')

tmax = 100

t_ = np.linspace(0, tmax, 10000)


with open("data.txt", "r") as DATA:
    data = DATA.read().splitlines()

DATA = []

for i in data:
    a = float(i)
    DATA.append(a)

alpha = (np.log(DATA[len(DATA)-1]/DATA[0]))/tmax

def temperature(t):
    s = DATA[0]*np.exp(alpha*t)
    return(s)

T = temperature(t_)
print(alpha)

t = np.linspace(0, tmax, len(data))

plt.plot(t, DATA, color = 'red', marker= 'x')
plt.plot(t_, T, color = 'blue')
plt.show()
