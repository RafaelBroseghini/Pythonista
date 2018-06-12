import sys
import time
import getch


MOVES = {"z":"x", "x":"z"}

def get_distance():
    while True:
        try:
            inp = int(input("How long will be your race today?: "))
            if isinstance(inp, int):
                return inp
        except:
            sys.stdout.write("Not a valid distance. Try again!\n")

def race(d):
    inp = getch.getche()
    correct = MOVES["x"]
    distance_ran = 0
    if inp == correct:
        distance_ran += 1
        start = time.time()
        while distance_ran < d:
            correct = MOVES[correct]
            while inp != correct:
                inp = getch.getche()
            else:
                distance_ran += 1
        end = time.time()
        return "\nFinished in: {:.3f}s".format(end-start)
    return "\nYou burned the lead!\n"

def main():
    distance = get_distance()

    sys.stdout.write("Use 'z' and 'x' back and forth to run! (START WITH 'z')\n")
    sys.stdout.write("Ready! Set! Go! {}m sprint!\n".format(distance))
    record = race(distance)
    print(record)

if __name__ == '__main__':
    main()