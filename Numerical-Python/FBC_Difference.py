import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2*np.pi, 100)
f = lambda x:np.sin(x)

def my_num_diff(f, a, b, n, option):
    if option == "Forward" :
        h = np.linspace(a,b,n)
        FD_main = []
        step = h[2]-h[1]
        r = len(h)
        for i in range(0,r) :
            FD = ( f(h[i]+step) - f(h[i]))/step
            FD_main.append(FD)
        XF = np.array([FD_main,h])
        return XF
    elif option == "Backward" :
        h = np.linspace(a,b,n)
        BD_main = []
        step = h[2]-h[1]
        r = len(h)
        for i in range(0,r) :
            BD = ( f(h[i]) - f(h[i] - step))/step
            BD_main.append(BD)
        XB = np.array([BD_main,h])
        return XB
    elif option == "Central" :
        h = np.linspace(a,b,n)
        CD_main = []
        step = h[2]-h[1]
        r = len(h)
        for i in range(0,r) :
            CD = ( f(h[i]+step) - f(h[i] - step))/(2*step)
            CD_main.append(CD)
        XC = np.array([CD_main,h])
        return XC

[Dyf,Xf] = my_num_diff(f, 0, 2*np.pi, 20, "Forward")
[Dyb,Xb] = my_num_diff(f, 0, 2*np.pi, 20, "Backward")
[Dyc,Xc] = my_num_diff(f, 0, 2*np.pi, 20, "Central")

print(Xf)
print(Dyf)

plt.figure(figsize=(12,8))
plt.plot(x,np.cos(x), label ="Analytical")
plt.plot(Xf,Dyf, label ="Forward")
plt.plot(Xb,Dyb, label ="Backward")
plt.plot(Xc,Dyc, label ="Central")
plt.title("Analytical and Numerical derivative of Sine")
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.legend()
plt.show()



