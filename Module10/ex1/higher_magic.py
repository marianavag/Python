from collections.abc import Callable
from typing import List, Tuple


def fireball(target: str, power: int) -> str:
    return f"Fireball hits {target} with {power} damage"


def heal(target: str, power: int) -> str:
    return f"Heal restores {target} for {power} HP"


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combined(target: str, power: int) -> Tuple[str, int]:
        return (spell1(target, power), spell2(target, power))
    return combined


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def amplified(target: str, power: int) -> str:
        return base_spell(target, power * multiplier)
    return amplified


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def conditional(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        return "Spell fizzled"
    return conditional


def spell_sequence(spells: List[Callable]) -> Callable:
    def sequence(target: str, power: int) -> List[str]:
        results = []
        for spell in spells:
            results.append(spell(target, power))
        return results
    return sequence


def main() -> None:
    print("\nTesting spell combiner...")
    combined = spell_combiner(fireball, heal)
    result = combined("Dragon", 30)
    print(f"Combined spell result: {result}")
    print("\nTesting power amplifier...")
    original_power = 10
    original_fireball = fireball("Dragon", original_power)
    print(f"Original spell result: {original_fireball}")
    mega_fireball = power_amplifier(fireball, 3)
    result_amplified = mega_fireball("Dragon", original_power)
    print(f"Amplified spell result: {result_amplified}")
    print("\nTesting conditional caster...")
    conditioned_spell = conditional_caster(
        lambda target, power: power > 20,
        heal
    )
    result_success = conditioned_spell("Dragon", 30)
    result_fail = conditioned_spell("Dragon", 10)
    print(f"With 30 power: {result_success}")
    print(f"With 10 power: {result_fail}")
    print("\nTesting spell sequence...")
    total_sequence = spell_sequence([fireball, heal])
    result_sequence = total_sequence("Dragon", 30)
    print(f"Sequence results: {result_sequence}")


if __name__ == "__main__":
    main()
