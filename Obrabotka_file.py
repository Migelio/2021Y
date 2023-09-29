import numpy as np
import matplotlib.pyplot as plt
import random as rn
import time


file = open(r'C:\myProgram\py\Mod_sys_Savkin\TR_var_7.txt', 'r')
data = file.readlines()
for i in range(len(data)):
    data[i] = data[i].split(',')
    #print(data[i][1])


giro = []
accel = []
time = []
x = []
y = []
for i in range(len(data)):
    giro.append([float(data[i][0]),float(data[i][1]), float(data[i][2])])
    accel.append([float(data[i][9]),float(data[i][10]), float(data[i][11])])
    time.append([float(data[i][-1])])
    x.append([float(data[i][9])* 180/ np.pi])
    y.append([float(data[i][10])* 180/ np.pi])



#print(v)
print(time[4])
print(giro[i][0])
fig, (ax1, ax2) = plt.subplots(2, 1)

ax1.plot(time, x)
ax2.plot(time, y)

ax1.set_title('Giro_x')
ax2.set_title('Giro_y')
ax1.grid()
ax2.grid()
plt.show()
