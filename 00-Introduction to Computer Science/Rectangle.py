"""
Purpose: Calculate area and perimeter of a rectangle given the length and width.

Author: Rafael Broseghini
Date: 03/04/2016

Filename: broseghiniRectangle.py
"""


def calculateArea(n1, n2):
    return n1 * n2


def calculatePerimeter(n1, n2):
    return n1 * 2 + n2 * 2


def displayResults(length, width):
    print("==============")
    print("Area: {0:d}".format(calculateArea(length, width)))
    print("Perimeter: {0:d}".format(calculatePerimeter(length, width)))
    print("==============")


def main():
    length = int(input("Enter length of rectangle: "))
    width = int(input("Enter width of rectangle "))

    areaResult = calculateArea(length, width)
    perimeterResult = calculatePerimeter(length, width)
    displayRectangleResult = displayResults(areaResult, perimeterResult)

    return displayRectangleResult


main()
