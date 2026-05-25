from typing import Any
from collections.abc import Callable
import functools
import time


def spell_timer(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        print(f"Casting {func.__name__}...")
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Spell completed in {(end - start):.3f} seconds")
        return result
    return wrapper


def power_validator(min_power: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            power = kwargs.get("power")
            if power is None:
                power = args[-1]
            if power is not None and power >= min_power:
                result = func(*args, **kwargs)
            else:
                return "Insufficient power for this spell"
            return result
        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    if attempt < max_attempts:
                        print(f"Spell failed, retrying... (attempt {attempt}/"
                              f"{max_attempts})")
            return f"Spell casting failed after {max_attempts} attempts"
        return wrapper
    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        clean_name = name.replace(" ", "")
        return len(clean_name) >= 3 and clean_name.isalpha()

    @power_validator(min_power=10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


def main() -> None:
    print("Testing spell timer...")

    @spell_timer
    def fireball(target: str, power: int) -> str:
        time.sleep(0.101)
        return "Fireball cast!"
    result = (fireball("fire", 10))
    print(f"Result: {result}")

    print()
    print("Testing retrying spell...")

    @retry_spell(max_attempts=3)
    def failed_spell(target: str, power: int) -> str:
        raise Exception("The spell failed!")
    result_retry = failed_spell("Dragon", 5)
    print(result_retry)
    print("Waaaaaaagh spelled !")

    print()
    print("Testing MageGuild...")
    guild = MageGuild()
    print(guild.validate_mage_name("Merlin"))
    print(guild.validate_mage_name("  "))
    print(guild.cast_spell("Lightning", 15))
    print(guild.cast_spell("Lightning", 9))


if __name__ == "__main__":
    main()
