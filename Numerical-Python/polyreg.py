import numpy as np
import matplotlib.pyplot as plt

x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8])
y = np.array([0, 0.8, 0.9, 0.1, -0.6, -0.8, -1, -0.9, -0.4])

plt.figure(figsize =(12,8))

for i in range (1, 9):

    y_est = np.polyfit(x,y,i)
    plt.subplot(3,3,i)
    plt.plot(x,y,"o")

    plt.plot(x, np.polyval(y_est,x))
    plt.title(f"Plynomial Order {i}")

plt.tight_layout()
plt.show()


