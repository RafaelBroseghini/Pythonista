'''
Purpose: Calculate area and perimeter of a rectangle given the length and width.

Author: Rafael Broseghini
Date: 03/04/2016

Filename: broseghiniRectangle.py
'''
# Function that calls all the other functions.
def main(): 
    length = int(input('Enter length of rectangle: '))
    width = int(input('Enter width of rectangle '))
    areaResult = calculateArea(length, width)
    perimeterResult = calculatePerimeter(length, width)
    print()
    displayRectangleResult = displayResults(length, width)

# Function that calculates and returns the area of a rectangle.
def calculateArea(n1, n2):
    return n1 * n2

# Function that calculates and returns the perimeter of a rectangle.
def calculatePerimeter(n1, n2): 
    return (n1*2 + n2*2)

# Function that returns a specific print statement containing the area and perimeter of a rectangle in its structuring.
def displayResults(length, width):
    print('Area: {0:d}'.format(calculateArea(length, width)))
    print('Perimeter: {0:d}'.format(calculatePerimeter(length, width)))
    
main()   # Executes main function. 
