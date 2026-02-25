import numpy as np
import matplotlib.pyplot as plt

g = 9.81
dt = 0.01 
tMax = 5.00 
steps = int(tMax / dt)

t = np.zeros(steps)
y = np.zeros(steps)
v = np.zeros(steps)

y[0] = 100.0
v[0] = 0.0

for i in range(steps - 1):
    v[i + 1] = v[i] - g * dt
    y[i + 1] = y[i] + v[i] * dt
    t[i + 1] = t[i] + dt

    if y[i + 1] < 0.0:
        y[i + 1] = 0.0
        v[i + 1] = -v[i + 1] * 0.8

plt.plot(t ,y)
plt.xlabel('Time (s)')
plt.ylabel('Height (m)')
plt.title('1D Bouncing Kinematics (Euler Method)')
plt.grid(True)

plt.savefig('trajectory.png')