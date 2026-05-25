from collections.abc import Callable
from typing import Any, List, Dict
import functools
import operator


def spell_reducer(spells: List[int], operation: str) -> int:
    if not spells:
        return 0
    if operation not in ["add", "multiply", "max", "min"]:
        raise ValueError("Unknown operation")
    operations = {
        "add": operator.add,
        "multiply": operator.mul,
        "max": lambda a, b: max(a, b),
        "min": lambda a, b: min(a, b)
    }
    func = operations[operation]
    return functools.reduce(func, spells)


def partial_enchanter(base_enchantment: Callable) -> Dict[str, Callable]:
    fire_ench = functools.partial(base_enchantment, power=50, element="fire")
    water_ench = functools.partial(base_enchantment, power=50, element="water")
    air_ench = functools.partial(base_enchantment, power=50, element="air")
    return {
        "fire": fire_ench,
        "water": water_ench,
        "air": air_ench
    }


@functools.lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n < 2:
        return n
    return memoized_fibonacci(n-1) + memoized_fibonacci(n-2)


def spell_dispatcher() -> Callable[[Any], str]:
    @functools.singledispatch
    def dispatcher(spell: Any) -> str:
        return "Unknown spell type"

    @dispatcher.register(int)
    def _(spell: int) -> str:
        return f"Damage spell: {spell} damage"

    @dispatcher.register(str)
    def _(enchantment: str) -> str:
        return f"Enchantment: {enchantment}"

    @dispatcher.register(list)
    def _(multi_cast: List) -> str:
        results = [dispatcher(s) for s in multi_cast]
        return ", ".join(results)
    return dispatcher


def main() -> None:
    print()
    print("Testing spell reducer...")
    spell_powers = [10, 20, 30, 40]
    try:
        print(f"Sum: {spell_reducer(spell_powers, 'add')}")
        print(f"Product: {spell_reducer(spell_powers, 'multiply')}")
        print(f"Max: {spell_reducer(spell_powers, 'max')}")
    except ValueError as e:
        print(f"Error: {e}")
    print()
    print("Testing partial enchanter...")

    def base_enchantment(power: int, element: str, target: str) -> str:
        element_forces = {
            "fire": "Blast",
            "water": "Torrent",
            "air": "Cyclone"
        }
        spell_type = element_forces.get(element, "Spell")
        return f"Elemental {spell_type} hit {target} for {power} damage!"

    ele_enchants = partial_enchanter(base_enchantment)
    print(f"Fire: {ele_enchants['fire'](target='Ice Giant')}")
    print(f"Water: {ele_enchants['water'](target='Ice Giant')}")
    print(f"Air: {ele_enchants['air'](target='Ice Giant')}")
    print()
    print("Testing memoized fibonacci...")
    print(f"Fib(0): {memoized_fibonacci(0)}")
    print(f"Fib(1): {memoized_fibonacci(1)}")
    print(f"Fib(10): {memoized_fibonacci(10)}")
    print(f"Fib(15): {memoized_fibonacci(15)}")
    print()
    print("Testing spell dispatcher...")
    disp_test = spell_dispatcher()
    print(disp_test(42))
    print(disp_test("fireball"))
    multi_spell = [42, "fireball", 3.14]
    print(f"Multi-cast: {len(multi_spell)} spells -> {disp_test(multi_spell)}")
    print(disp_test(3.14))


if __name__ == "__main__":
    main()
