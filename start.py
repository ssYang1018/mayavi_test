from mayavi import mlab

x = [-1, 0, 0, 0, 1]
y = [0, -1, 0, 1, 0]
z = [0, 0, 3, 0, 0]
triangular = [(2, 0, 1), (2, 1, 3), (2, 3, 4), (2, 4, 0)]

mlab.triangular_mesh(x, y, z, triangular)
mlab.axes()
mlab.outline()
mlab.show()
