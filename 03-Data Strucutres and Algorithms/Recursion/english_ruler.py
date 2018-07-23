# Implementation of the enlish ruler drawing, recursively.

'''
Each call to draw interval, calls itself twice 
until ticklength = 0, drawing the line in between.
'''


def draw_line(length, tick_mark=''):
    line = '-'*length + tick_mark
    return line

def draw_interval(length):
    # Base case.
    if length > 0:
        # Recursive calls and moving towards the base case.
        draw_interval(length-1)
        print(draw_line(length))
        draw_interval(length-1)


def draw_ruler(inches, length):
    print(draw_line(length, ' 0'))

    for i in range(1, inches+1):
        draw_interval(length-1)
        print(draw_line(length), str(i))


def main():
    draw_ruler(2, 4)

if __name__ == '__main__':
    main()