#!/usr/bin/python3
#A module to calculate an equation of a polynomial from a set of points
#The number of points on the equation required is equal to one more than the polynomial degree

#------Imports------
import numpy

#------Procedures/Functions------
#Creates the matrix that allows calculation of the polynomail
#Arguments: -xPoints, a list of x-axis points in the equation
#           -The polynomail degree
#Returns:   -A numpy array containing the matrix representation of the a, b, c ... coefficients, i.e. the simultaneous equation coefficients
def getMatrix(_xPoints, _polyDegree):
    polyMatrix = []
    #Adds each form of the polynomial to the equation
    #In form of: ax^n + bx^(n-1) + cx^(n-2) ...
    for i in range(len(_xPoints)):
        #Calculates one row with one value of x
        row = []
        for j in range(_polyDegree + 1):
            row.append(_xPoints[i] ** (_polyDegree - j))
        #Adds the row to the matrix
        polyMatrix.append(row)
    #Converts the matrix to a numpy array and returns it
    return numpy.array(polyMatrix)

#Calculates a polynomial equation that goes through all points
#Works out the polynomial degree from the given points
#Arguments: -A list of points, each point being an (x, y) tuple
def calculatePolynomail(_points):
    if type(_points) != list: raise Exception("Points must be a list")
    #Calculates the polynomial degree, length of points - 1
    polyDegree = len(_points) - 1
    #Seperates the list into a seperate list of x and y points
    xPoints = []
    yPoints = []
    for i in range(len(_points)):
        if len(_points[i]) != 2: raise Exception("Length of point at index %s is not 2"%i)
        xPoints.append(_points[i][0])
        yPoints.append(_points[i][1])
    #Gets the simultaneous equation coefficients
    simulEquation = getMatrix(xPoints, polyDegree)
    #Calculates the coefficients of the polynomial equation by solving the simultaneous equation
    coefficients = numpy.dot(numpy.linalg.inv(simulEquation), numpy.array(yPoints).T)
    #Returns the coefficients of the polynomial equation
    return coefficients
    


if __name__ == "__main__":
    #Creates points on an example polynomial with coefficients:
    coefficients = [4, 2, 6, 2, -2, -1, -6, 7, 9, 4]
    points = []
    for x in range(10):
        y = 0
        for power in range(10):
            y += coefficients[power] * (x ** (10 - 1 - power))
        points.append((x, y))
    print("------Example 1------")
    print(coefficients)
    print(calculatePolynomail(points))

    print("------Example 2------")
    points = [(10, 4), (15, 8), (6, 4), (4.7, 9)]
    print(points)
    print(calculatePolynomail(points))