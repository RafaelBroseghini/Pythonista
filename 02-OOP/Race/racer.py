from track import Track
from car import Car


def lets_race(drivers=[Car("Rarri"), Car("Tesla")]) -> str:
    t = Track()
    done = False
    while not done:
        for d in drivers:
            print(d)
            d.accelerate()
            t.check_winner(d)

            if t.winner:
                done = True

    return "And the winner is: {}".format(t.winner)


def main():
    print(lets_race())


if __name__ == "__main__":
    main()
