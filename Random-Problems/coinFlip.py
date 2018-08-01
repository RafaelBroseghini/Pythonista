import random
import sys

def flip(ntimes):
    ftdict = {"Heads": 0, "Tails": 0}
    for f in range(ntimes):
        f = random.randint(0,1)
        if f == 0:
            ftdict["Heads"] += 1
        else:
            ftdict["Tails"] += 1
    
    return ftdict

def display_output():
    try:
        total_flips = flip(int(sys.argv[1]))
        sys.stdout.write("Heads: {}\n".format(total_flips["Heads"]))
        sys.stdout.write("Tails: {}\n".format(total_flips["Tails"]))
        return True
    except ValueError as error:
        print("Error:", error)


def main():
    display_output()

if __name__ == '__main__':
    main()
