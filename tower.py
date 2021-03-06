import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate

#########


#with open('droptower_vdata.txt') as f:
  #  for line in f:
x,y = np.loadtxt('droptower_vdata.txt', unpack = True)
print(x)
print(y)

fig = plt.figure()
fig.suptitle('Velocity')
plt.plot(x,y, marker='o')
plt.show()
fig.savefig('velocity.jpg')

iy = integrate.cumtrapz(y, x, initial=0)

fig = plt.figure()
fig.suptitle('Position')
plt.plot(x,iy, marker='o')
plt.show()
fig.savefig('Position.jpg')

dy = np.diff(y)

dx= np.delete(x,-1)
print(dx)

fig = plt.figure()
fig.suptitle('Acceleration')
plt.plot(dx,dy, marker='o')
plt.show()
fig.savefig('Acceleration.jpg')

fig = plt.figure()
fig.suptitle('All 3')
plt.plot(x,y, color='r', marker='o', label='Velocity')
plt.plot(x,iy, color = 'b', marker='v', label='Displacement')
plt.plot(dx,dy, color = 'g', marker = '^', label = 'Acceleration')
plt.legend(scatterpoints=1, loc ='best')
plt.show()
fig.savefig('All3sameGraph.jpg')

fig, axarr = plt.subplots(3, sharex=True, sharey=True)
axarr[0].plot(x,y,color='r')
axarr[1].plot(x,iy,color='b')
axarr[2].plot(dx,dy,color='g')
axarr[0].set_title('Velocity')
axarr[1].set_title('Posititon')
axarr[2].set_title('Acceleration')
plt.tight_layout()
fig.suptitle("All on same pair of axes", size = 15)
plt.subplots_adjust(top=0.85)
plt.show()
fig.savefig('All3sameAxes.jpg')
