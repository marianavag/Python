from ex0 import CreatureFactory
from ex1 import TransformCreatureFactory
from ex2 import BattleStrategy, InvalidStrategyError


def battle(opponents: List[Tuple[CreatureFactory, BattleStrategy]]) -> None:
    combatants = []
    for factory, strategy in opponents:
        creature = factory.create_base()
        combatants.append((creature, strategy))
    for i in range(len(combatants)):
        for j in range(i + 1, len(combatants)):
            c1, s1 = combatants[i]
            c2, s2 = combatants[j]
            print("* Battle *")
            print(c1.describe())
            print(" vs.")
            print(c2.describe())
            print(" now fight!")
            try:
                print(s1.act(c1))
                print(s2.act(c2))
            except InvalidStrategyError as e:
                print(f"Battle error, aborting tournament: {e}")
            print()


if __name__ == "__main__":
    
