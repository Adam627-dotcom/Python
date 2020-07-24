# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 13:06:12 2020 

@author: Goinesa1
"""
#Contributor/sources
#Dylan Flaute, 
#https://stackoverflow.com/questions/29512046/how-to-create-ternary-contour-plot-in-python
# Simple Numerical Laplace Equation Solution using Finite Difference Method
#
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 15:29:47 2020

@author: Goinesa1
"""

# Python Version of Matlab 'Research.m'
# Simple Numerical Laplace Equation Solution using Finite Difference Method
import matplotlib.pyplot as plt
import matplotlib.tri as tri
import numpy as np

# create the grid
tri_x = 4.32
tri_y = tri_x / 2
corners = np.array([[0, 0], [tri_x, 0], [tri_x / 2, tri_y]])
triangle = tri.Triangulation(corners[:, 0], corners[:, 1])

# creating the grid
refiner = tri.UniformTriRefiner(triangle)
trimesh = refiner.refine_triangulation(subdiv=4)
print(corners)
print(triangle)
#plotting the mesh
plt.triplot(trimesh,'k--')

# Set maximum iteration
maxIter = 500

# Set Dimension and delta
# lenY =int(4.32)
# lenX = int(3.05)#we set it triangle in cm**2
lenY = max(tri_x, tri_y)
lenX = max(tri_x, tri_y)
# delta = 1

# Boundary condition
Ttop = 0
Tbottom = 330.15
Tleft = 0
Tright = 0

# Initial guess of interior grid
Tguess = 30

# Set colour interpolation and colour map
colorinterpolation = 500
colourMap = plt.cm.jet #you can try: colourMap = plt.cm.coolwarm

# Set meshgrid
# NOTE: You could set the number of samples here as an extra arg to linspace
X, Y = np.meshgrid(np.linspace(0,lenX), np.linspace(0, lenY))
print(X,Y)
n_x, n_y = X.shape #tells how many samples you have

# Set array size and set the interior value with Tguess
T = np.empty_like(X)
T.fill(Tguess)

# Set Boundary condition
T[1:, :] = Ttop
T[:1, :] = Tbottom
T[:, -1:] = Tright
T[:, :1] = Tleft

# Iteration (We assume that the iteration is convergence in maxIter = 500)
print("Please wait for a moment")

for iteration in range(0, maxIter):
    for i in range(1, n_x-1):
        for j in range(1, n_y-1):
            T[i, j] = 0.25 * (T[i+1][j] + T[i-1][j] + T[i][j+1] + T[i][j-1])

print("Iteration finished")
print(T[i, j])
# Configure the contour
plt.title("Contour of Temperature")
print("!!!!!!!!!!!!", X)
print("!!!!!!!!!!!!", Y)
print("!!!!!!!!!!!!", T)

plt.contourf(X, Y, T, colorinterpolation, cmap=colourMap)

# Set Colorbar
plt.colorbar()

# Show the result in the plot window
plt.show()

print("")