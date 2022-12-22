from collections import defaultdict

from battles.character import Character


class Combat:

    def __init__(self, *roster: Character):
        self.roster = list(roster)
        self.history = defaultdict(int)

    def combat(self, *roster: Character):
        assert len(roster) > 1, "The roster must contain at least 2 characters!"
        battle_field = {unit.name: unit() for unit in roster}
        highest = max(battle_field.values())
        winners = [
            character for character in roster
            if battle_field[character.name] == highest
        ]
        if len(winners) == 1:
            winner, *_ = winners
            self.history[winner.name] += 1
            return winner
        else:
            return self.combat(*winners)

    def __call__(self, n_rounds):
        for _ in range(n_rounds):
            self.combat(*self.roster)

    def __str__(self):
        return "\n".join(f"{k}: {v}" for k, v in self.history.items())
