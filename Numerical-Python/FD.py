import numpy as np
import matplotlib.pyplot as plt

h=0.1
x = np.arange(0, 2*np.pi, h)
print(x)
y = np.cos(x)

f_diff = np.diff(y)/h

x_diff = x[:-1:]  # last term wont be counted as its FD
print(x_diff)
exact_sol = -np.sin(x)


plt.figure(figsize=(12,8))
plt.plot(x_diff,f_diff, "--g", label ="Finite difference approximation")
plt.plot(x,exact_sol, "r", label ="Exact solution")
plt.legend()
plt.show()



