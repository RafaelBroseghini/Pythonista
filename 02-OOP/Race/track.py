from car import Car


class Track(object):
    def __init__(self, total_distance=3000):
        self._total_distance = total_distance
        self._winner = None

    @property
    def total_distance(self) -> int:
        return total_distance

    @property
    def winner(self) -> str:
        return self._winner

    def check_winner(self, contestant: Car) -> bool:
        if not isinstance(contestant, Car):
            raise Exception("Only cars can race.")

        if contestant.distance >= self._total_distance:
            self._winner = contestant
            return True
