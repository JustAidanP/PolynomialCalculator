#!/usr/bin/python3
"""
A module to calculate an equation of a polynomial that goes through the set of points given
The number of points on the equation required is equal to one more than the polynomial degree
"""
import numpy as np


def _get_matrix(x_points: list[float], polynomial_degree: int) -> np.ndarray:
    """
    Creates the matrix that allows calculation of the polynomial

    :param x_points: A list of values in the x-axis
    :type x_points: list[float]
    :param polynomial_degree: The polynomial degree
    :type polynomial_degree: int
    :return: A matrix that'll be used to solve for the polynomial coefficients
    :rtype: np.ndarray
    """

    poly_matrix = []
    # Adds each form of the polynomial to the equation
    # In form of: ax^n + bx^(n-1) + cx^(n-2) ...
    for i in range(len(x_points)):
        # Calculates one row with one value of x
        row = []
        for j in range(polynomial_degree + 1):
            row.append(x_points[i] ** (polynomial_degree - j))
        # Adds the row to the matrix
        poly_matrix.append(row)
    # Converts the matrix to a numpy array and returns it
    return np.array(poly_matrix)


def calculate_polynomial(points: list[tuple[float, float]]):
    """
    Calculates a polynomial equation that goes through all points

    :param points: The x,y points that the equation must satisfy
    :type points: list[tuple[float, float]]
    :return: The coefficients of the polynomial
    :rtype: np.ndarray

    :raise: TypeError("Points must be a list")
    :raise: ValueError(f"Length of point at index {i} is not 2")
    """
    if type(points) != list:
        raise TypeError("Points must be a list")
    # Calculates the polynomial degree, length of points - 1
    poly_degree = len(points) - 1
    # Separates the list into a separate list of x and y points
    x_points = []
    y_points = []
    for i in range(len(points)):
        if len(points[i]) != 2:
            raise ValueError(f"Length of point at index {i} is not 2")
        x_points.append(points[i][0])
        y_points.append(points[i][1])
    # Gets the simultaneous equation coefficients
    simultaneous_equation = _get_matrix(x_points, poly_degree)
    # Calculates the coefficients of the polynomial equation by solving the simultaneous equation
    coefficients = np.dot(np.linalg.inv(simultaneous_equation), np.array(y_points).T)
    # Returns the coefficients of the polynomial equation
    return coefficients


if __name__ == "__main__":
    # Creates points on an example polynomial with coefficients:
    coefficients = [4, 2, 6, 2, -2, -1, -6, 7, 9, 4]
    points = []
    for x in range(10):
        y = 0
        for power in range(10):
            y += coefficients[power] * (x ** (10 - 1 - power))
        points.append((x, y))
    print("------Example 1------")
    print(coefficients)
    print(calculate_polynomial(points))

    print("------Example 2------")
    points = [(10, 4), (15, 8), (6, 4), (4.7, 9)]
    print(points)
    print(calculate_polynomial(points))
