import numpy as np
from scipy.integrate import quad
import matplotlib.pyplot as plt

def my_fourier_coef(f,n):
    #funcA = f*np.cos
    #funcB = f*np.sin
    C = lambda x:f(x)*np.cos(n*x)
    s = lambda x:f(x)*np.sin(n*x)
    A_n,A_n_error = quad(C, -np.pi, np.pi)
    B_n,B_n_error = quad(s, -np.pi, np.pi)
    A_n = A_n*(1/np.pi)
    B_n = B_n*(1/np.pi)
    return [A_n,B_n]
def plot_results(f,N):
    x = np.linspace(-np.pi,np.pi,100)
    [A0,B0] = my_fourier_coef(f,0)
    y = A0*np.ones(len(x))/2

    for n in range (1,N):
        [An,Bn] = my_fourier_coef(f,n)
        y += An*np.cos(n*x)+Bn*np.sin(n*x)

    plt.figure(figsize=(12,8))
    plt.plot(x,f(x), label ="Analytical")
    plt.plot(x,y, label ="approximate")
    plt.title(f"{N}th Order Fourier Approximation")
    plt.xlabel("X axis")
    plt.ylabel("Y axis")
    plt.legend()
    plt.show()

f = lambda x:np.sin(np.exp(x))
#f = lambda x:np.mod(x,np.pi/2)
N = 20
plot_results(f,N)