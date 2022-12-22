from battles.battle import Combat
from battles.character import Character


combat = Combat(
    Character("Alpha", bonus=0),
    Character("Kappa", bonus=1),
    Character("Gamma", bonus=2),
    Character("Delta", bonus=3),
)
n_rounds = 1000
combat(n_rounds)
print(f"After {n_rounds} rounds of combat:\n{combat}")
