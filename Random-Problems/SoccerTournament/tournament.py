import team, player, random
class Tournament():
    def __init__(self, teams=[[],[],[],[],[],[]], validator = {}, winner = None):
        self._winner = winner
        self._teams = teams
        self._validator = validator

    @property
    def winner(self):
        return self._winner

    @property
    def teams(self):
        return self._teams
    
    @property
    def validator(self):
        return self._validator

    def make_teams(self, roster):
        j = 1
        i = 0
        print(len(roster))
        while j <= 30:
            p = random.choice(roster)
            if p not in self.validator and len(self.teams[i]) < 6:
                self.validator[p] = "used"
                self.teams[i].append(p)
                j += 1
                i += 1
                if i > 5:
                    i = 0 

        return self.teams

    def compute_winner(self):
        ms = 0
        t = 0
        for team in range(len(self.teams)):
            score = 0
            for p in range(len(self.teams[team])):
                score += self.teams[team][p].score
            if score > ms:
                ms = score
                t = team

        return self.teams[t]