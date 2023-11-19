import numpy as np
import matplotlib.pyplot as plt

# Explicit Euler 

f = lambda t,s:np.exp(-t) #ODE

h = 0.01 #STEP SIZE
t = np.arange(0,h+1,h)
s0 = -1 #INITIAL CONDITION

s = np.zeros(len(t)) 
s[0] = s0 

for i in range (0, len(t)-1):
    s[i+1] = s[i] + h*f(t[i],s[i])

plt.figure(figsize=(12,8))
plt.plot(t,s , "b--", label = "Approximate")
plt.plot(t,-np.exp(-t) , "g", label = "Exact")
plt.title("Approximate and exact solution for ODE")
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.grid()
plt.legend()
plt.show()
