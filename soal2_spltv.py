import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

# set initial array based on mathematical equation
a = np.array([[1, -2, 1], [3, 1, -2], [7, -6, -1]])
b = np.array([6, 4, 10])

# get the x, y, z values
c = np.linalg.solve(a, b)

print('Nilai x = {}'.format(c[0].round(1)))
print('Nilai y = {}'.format(c[1].round(1)))
print('Nilai z = {}'.format(c[2].round(1)))

# state the initial array condition
x1 = np.array([6, 0, 0])
y1 = np.array([0, -3, 0])
z1 = np.array([[0, 0, 6]])

x2 = np.array([1.3333, 0, 0])
y2 = np.array([0, 4, 0])
z2 = np.array([[0, 0, -2]])

x3 = np.array([1.43, 0, 0])
y3 = np.array([0, -1.67, 0])
z3 = np.array([[0, 0, -10]])

plt.figure('Lat-SPLV', figsize=(15,5))

# plot first 3D
my_plot = plt.subplot(131, projection = '3d')   #subplot bisa dimasukkan di dalam variabel
my_plot.plot_wireframe(x1, y1, z1, facecolor = 'red', alpha = 0.3)
my_plot.scatter(x1, y1, z1, color = 'blue', s = 50)
my_plot.set_title('x - 2y + z = 6')
my_plot.set_xlabel('Nilai x')
my_plot.set_ylabel('Nilai y')
my_plot.set_zlabel('Nilai z')

# plot second 3D
my_plot = plt.subplot(132, projection = '3d')   #subplot bisa dimasukkan di dalam variabel
my_plot.plot_wireframe(x2, y2, z2, facecolor = 'yellow', alpha = 0.3)
my_plot.scatter(x2, y2, z2, color = 'red', s = 50)
my_plot.set_title('3x + y - 2z = 4')
my_plot.set_xlabel('Nilai x')
my_plot.set_ylabel('Nilai y')
my_plot.set_zlabel('Nilai z')

# plot third 3D
my_plot = plt.subplot(133, projection = '3d')   #subplot bisa dimasukkan di dalam variabel
my_plot.plot_wireframe(x3, y3, z3, facecolor = 'blue', alpha = 0.3)
my_plot.scatter(x3, y3, z3, color = 'green', s = 50)
my_plot.set_title('7x - 6y - z = 10')
my_plot.set_xlabel('Nilai x')
my_plot.set_ylabel('Nilai y')
my_plot.set_zlabel('Nilai z')

# adjust subplot arrangement
plt.subplots_adjust(left = 0, right = 0.97, wspace = 0.1)

plt.show()