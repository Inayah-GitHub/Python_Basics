"""
This exercise tests the use of:
* conditional statements 
* console I/O
* functions
* setting axises sizes and labels 
"""
import math 
from matplotlib import pyplot as plt

# Defining a function that draws a regular polygon on the axis 
# Params = the number of sides (n), side lengths (l) and a centrepoint (xc,yc)
def reg_polygon(xc, yc, n, l):
    # Validation of input numbers 
    if n < 3:
        exit()
    elif l <= 0:
        exit()
    # Creating two empty lists for storing points later  
    xp = []
    yp = []
    # Loop to calculate the points needed 
    for i in range(n+1):
        # r specifies the distance of each vetex from the centrepoint given a sidelength l 
        r = l / (2*math.sin(math.pi/n))
        # The coordinates of the ith point are given by 
        xi = xc + r*math.sin((2*math.pi*i) / n)
        xp.append(xi)
        yi = yc + r*math.cos((2*math.pi*i) / n)
        yp.append(yi)
    plt.plot(xp, yp, 'r-')

# Set axis to be a square 
plt.axis('square')
# Set axis limits to be x: 0-400 and y: 0-400
plt.axis([0,400,0,400])
# Set the title to be 'Polygons'
plt.title('Polygons')
# Set the titles for the x and y axis
plt.xlabel('x axis')
plt.ylabel('y axis')

# Draw 3 polygons using this code  
reg_polygon(xc=100 ,yc=100 ,n=3 ,l=100)
reg_polygon(xc=200 ,yc=200 ,n=5 ,l=75)
reg_polygon(xc=300 ,yc=300 ,n=7 ,l=50)
# Saving the image as 'Polygons.png'
plt.savefig('Polygons')
