import numpy as np
from numpy.linalg import inv
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt


# define step size
h = 0.1
# define numerical grid
t = np.arange(0, 20, h)

k = 10
m = 1
c =1
M = np.array([[0, 1], [-k/m, -c/m]])
def ode_func(t,x):
 return np.dot(M,x)

# Properties of MSD
k = 10
m = 1
c =1
s0 = np.array([[1], [0]])
m_e = np.array([[1, h],
[-k*h/m, -c*h/m+1]])

m_i = inv(np.array([[1, -h],
[k*h/m, c*h/m+1]]))

s_e = np.zeros((len(t), 2))
s_i = np.zeros((len(t), 2))

# do integrations
s_e[0, :] = s0.T
s_i[0, :] = s0.T

for j in range(0, len(t)-1):
 s_e[j+1, :] = np.dot(m_e,s_e[j, :])
 s_i[j+1, :] = np.dot(m_i,s_i[j, :])

# RK4 solve
solution_ivp = solve_ivp(ode_func,(0,20),(1,0),t_eval=t)
xRK4 = solution_ivp.y

 
plt.figure(figsize = (12, 8))
plt.plot(t,s_e[:,0],"g:")
plt.plot(t,s_i[:,0],"r:")
plt.plot(t,xRK4[0,:],"b-")
plt.ylim([-1.2, 1.2])
plt.xlabel("t")
plt.ylabel("Amplitude")
plt.legend(["Explicit","Implicit","RK4 solve"])
plt.show()