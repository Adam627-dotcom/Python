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
corners = np.array([[0, 0], [int(4.32), 0], [int(0.5*4.32),  2.16]])
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
lenY =int(4.32)
lenX = int(3.05)#we set it triangle in cm**2
delta = 1

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
X, Y = np.meshgrid(np.arange(0,lenX), np.arange(0, lenY))
print(X,Y)
#np.meshgrid(np.arange(0,lenX), np.arange(0, lenY))

# Set array size and set the interior value with Tguess
T = np.empty((lenX,lenY))
T.fill(Tguess)

# Set Boundary condition
T[(lenY-1):, :] = Ttop
T[:1, :] = Tbottom
T[:, (lenX-1):] = Tright
T[:, :1] = Tleft

# Iteration (We assume that the iteration is convergence in maxIter = 500)
print("Please wait for a moment")

for iteration in range(0, maxIter):
    for i in range(1, lenX-1, delta):
        for j in range(1, lenY-1, delta):
            T[i, j] = 0.25 * (T[i+1][j] + T[i-1][j] + T[i][j+1] + T[i][j-1])

print("Iteration finished")
print(T[i, j])
# Configure the contour
plt.title("Contour of Temperature")
plt.contourf(X.reshape(4,3), Y.reshape(4,3), T.reshape(4,3), colorinterpolation, cmap=colourMap)

# Set Colorbar
plt.colorbar()

# Show the result in the plot window
plt.show()

print("")