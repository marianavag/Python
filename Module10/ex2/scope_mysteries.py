from collections.abc import Callable
from typing import Any, Dict


def mage_counter() -> Callable:
    count = 0

    def counter() -> int:
        nonlocal count
        count += 1
        return count

    return counter


def spell_accumulator(initial_power: int) -> Callable:
    current_power = initial_power

    def accumulator(extra_power: int) -> int:
        nonlocal current_power
        current_power += extra_power
        return current_power

    return accumulator


def enchantment_factory(enchantment_type: str) -> Callable:
    def enchant(item_name: str) -> str:
        return f"{enchantment_type} {item_name}"
    return enchant


def memory_vault() -> Dict[str, Callable]:
    vault = {}

    def store(key: str, value: Any) -> None:
        vault[key] = value

    def recall(key: str) -> Any:
        return vault.get(key, "Memory not found")

    return {"store": store, "recall": recall}


def main() -> None:
    print("Testing mage counter...")
    counter_a = mage_counter()
    print(f"counter_a call 1: {counter_a()}")
    print(f"counter_a call 2: {counter_a()}")
    counter_b = mage_counter()
    print(f"counter_b call 1: {counter_b()}")
    print()
    print("Testing spell accumulator...")
    base = spell_accumulator(100)
    print(f"Base 100, add 20: {base(20)}")
    print(f"Base 100, add 30: {base(30)}")
    print()
    print("Testing enchantment factory...")
    ench_1 = enchantment_factory("Flaming")
    print(f'{ench_1("Sword")}')
    ench_2 = enchantment_factory("Frozen")
    print(f'{ench_2("Shield")}')
    print()
    print("Testing memory vault...")
    inside_vault = memory_vault()
    print("Store 'secret' = 42")
    inside_vault["store"]("secret", 42)
    print(f"Recall 'secret': {inside_vault['recall']('secret')}")
    print(f"Recall 'unknown': {inside_vault['recall']('unknown')}")


if __name__ == "__main__":
    main()
