import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from scipy.integrate import solve_ivp

sigma = 10
rho = 28
beta = 8/3

def my_lorenz(t,x):
    dx = [sigma*(x[1]-x[0]),x[0]*(rho-x[2])-x[1]
        ,(x[0]*x[1])-(beta*x[2])]
    dX = np.array(dx)
    return dX
x0 = np.array([-8, 8, 27])


h = 0.01
t_e = 30
t = np.arange(0,t_e,h)


solution = solve_ivp(my_lorenz,(0,t_e),x0,t_eval=t)
t = solution.t
y= solution.y.T

fig = plt.figure(figsize = (10,10))
ax = plt.axes(projection="3d")
ax.grid()
ax.plot3D(y[:,0], y[:,1], y[:,2])
ax.set_title("Lorenz")
# Set axes label
ax.set_xlabel("x", labelpad=20)
ax.set_ylabel("y", labelpad=20)
ax.set_zlabel("z", labelpad=20)
plt.show()
