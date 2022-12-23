from collections import defaultdict

from battles.units import Character


class BattleField:

    def __init__(self, *roster: Character):
        self.roster = list(roster)
        self.history = defaultdict(int)

    def _battle(self, *roster: Character):
        assert len(roster) > 1, "The roster must contain at least 2 characters!"
        field = {unit.name: unit() for unit in roster}
        winners = [
            character for character in roster
            if field[character.name] == max(field.values())
        ]
        if len(winners) == 1:
            winner, *_ = winners
            self.history[winner.name] += 1
            return winner
        else:
            return self._battle(*winners)

    def __call__(self, n_rounds: int):
        for _ in range(n_rounds):
            self._battle(*self.roster)
        return self

    def __str__(self):
        output = sorted((
            (k, v) for k, v in self.history.items()
        ), key=lambda x: x[1], reverse=True)
        return "\n".join(f"{k}: {v}" for k, v in output)

    def __repr__(self):
        return str(self)
