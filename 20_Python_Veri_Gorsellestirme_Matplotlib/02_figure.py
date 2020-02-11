import matplotlib.pyplot as plt
import numpy as np
"""
x = np.linspace(-10,9,20)
y = x ** 3
z = x ** 2

figure = plt.figure()
axes_cube = figure.add_axes([0.1,0.1,0.8,0.8])
axes_cube.plot(x,y,"b")
axes_cube.set_xlabel("x axis")
axes_cube.set_ylabel("y axis")
axes_cube.set_title("Cube")


axes_square = figure.add_axes([0.15,0.6,0.25,0.25])
axes_square.plot(x,z,"r")
axes_square.set_xlabel("x axis")
axes_square.set_ylabel("y axis")
axes_square.set_title("Square")

plt.show()
"""
"""
x = np.linspace(-10,9,20)
y = x ** 3
z = x ** 2

figure = plt.figure()
axes = figure.add_axes([0,0,1,1])
axes.plot(x,z,label="Square")
axes.plot(x,y,label="Cube")

axes.legend(loc=4)

plt.show()
"""
x = np.linspace(-10, 9, 20)
y = x ** 3
z = x ** 2

# fig,(axes1,axes2) = plt.subplots(nrows = 2, ncols=1,figsize=(8,8))
fig, (axes1, axes2) = plt.subplots(nrows=2, ncols=1, figsize=(4, 4))

axes1.plot(x, y)
axes1.set_title("Cube")

axes2.plot(x, z)
axes2.set_title("Square")

plt.tight_layout()
# fig.savefig("figure1.png")
fig.savefig("figure1.pdf")
plt.show()
