from typing import List, Tuple
from ex0 import FlameFactory, AquaFactory, CreatureFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import (
    BattleStrategy,
    InvalidStrategyError,
    NormalStrategy,
    AggressiveStrategy,
    DefensiveStrategy
)


def battle(opponents: List[Tuple[CreatureFactory, BattleStrategy]]) -> None:
    combatants = []
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")
    for factory, strategy in opponents:
        creature = factory.create_base()
        combatants.append((creature, strategy))
    for i in range(len(combatants)):
        for j in range(i + 1, len(combatants)):
            c1, s1 = combatants[i]
            c2, s2 = combatants[j]
            print()
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
                return


if __name__ == "__main__":
    try:
        flame_f = FlameFactory()
        aqua_f = AquaFactory()
        heal_f = HealingCreatureFactory()
        transf_f = TransformCreatureFactory()

        normal_s = NormalStrategy()
        agress_s = AggressiveStrategy()
        defensive_s = DefensiveStrategy()

        print("Tournament 0 (basic)")
        opponents_0 = [
            (flame_f, normal_s),
            (heal_f, defensive_s)
        ]
        print(" [ (Flameling+Normal), (Healing+Defensive) ]")
        battle(opponents_0)

        print()
        print("Tournament 1 (error)")
        print(" [ (Flameling+Aggressive), (Healing+Defensive) ]")
        opponents_1 = [
            (flame_f, agress_s),
            (heal_f, defensive_s)
        ]
        battle(opponents_1)

        print()
        print("Tournament 2 (multiple)")
        print(" [ (Aquabub+Normal), (Healing+Defensive), "
              "(Transform+Aggressive) ]")
        opponents_2 = [
            (aqua_f, normal_s),
            (heal_f, defensive_s),
            (transf_f, agress_s)
        ]
        battle(opponents_2)
    except Exception as e:
        print(f"Unexpected error: {e}")
