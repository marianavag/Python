import ex0


def factory_test(factory: ex0.CreatureFactory) -> None:
    print("Testing factory")
    base = factory.create_base()
    evolved = factory.create_evolved()
    print(base.describe())
    print(base.attack())
    print(evolved.describe())
    print(evolved.attack())


def battle_test(f1: ex0.CreatureFactory, f2: ex0.CreatureFactory) -> None:
    print("Testing battle")
    c1 = f1.create_base()
    c2 = f2.create_base()
    print(c1.describe())
    print(" vs.")
    print(c2.describe())
    print(" fight!")
    print(c1.attack())
    print(c2.attack())
    return


if __name__ == "__main__":
    flame_factory = ex0.FlameFactory()
    aqua_factory = ex0.AquaFactory()
    factory_test(flame_factory)
    print()
    factory_test(aqua_factory)
    print()
    battle_test(flame_factory, aqua_factory)
