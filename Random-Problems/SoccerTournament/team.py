class Team():
    def __init__(self, players=[], score = 0):
        self._players = players
        self._score = score

    @property
    def players(self):
        return self._players

    def compute_score(self):
        for p in range(len(self.players)):
            self.score += self.players[p].score