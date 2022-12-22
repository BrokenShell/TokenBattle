from Fortuna import dice


class Character:

    def __init__(self, name: str, bonus: int = 0):
        self.name = name
        self.bonus = bonus

    def __call__(self):
        return dice(1, 20) + self.bonus

    def __str__(self):
        return f"{self.name} +{self.bonus}"
