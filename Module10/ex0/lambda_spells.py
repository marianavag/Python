from typing import List, Dict


def artifact_sorter(artifacts: List[Dict]) -> List[Dict]:
    return sorted(artifacts, key=lambda item: item["power"], reverse=True)


def power_filter(mages: List[Dict], min_power: int) -> List[Dict]:
    return List(filter(lambda mage: mage["power"] >= min_power, mages))


def spell_transformer(spells: List[str]) -> List[str]:
    return List(map(lambda spell: "* " + spell + " *", spells))


def mage_stats(mages: List[Dict]) -> Dict:
    if not mages:
        return {"max_power": 0, "min_power": 0, "avg_power": 0.0}
    max_power = max(mages, key=lambda m: m["power"])["power"]
    min_power = min(mages, key=lambda m: m["power"])["power"]
    avg_power = round(sum(map(lambda m: m["power"], mages)) / len(mages), 2)
    return {
        "max_power": max_power,
        "min_power": min_power,
        "avg_power": avg_power
        }


def main() -> None:
    artifacts = [
        {"name": "Crystal Orb", "power": 85, "type": "Focus"},
        {"name": "Fire Staff", "power": 92, "type": "Weapon"},
        {"name": "Invisibility Cloak", "power": 81, "type": "Armor"}
    ]
    mages = [
        {"name": "Merlin", "power": 90, "element": "Fire"},
        {"name": "Aria", "power": 75, "element": "Water"},
        {"name": "Morgana", "power": 82, "element": "Dark"}
    ]
    spells = ["fireball", "heal", "shield"]
    print("\nTesting artifact sorter...")
    try:
        sorted_arts = artifact_sorter(artifacts)
        art_0 = sorted_arts[0]
        art_1 = sorted_arts[1]
        print(
            f"{art_0['name']} ({art_0['power']} power) comes before "
            f"{art_1['name']} ({art_1['power']} power)"
        )
    except KeyError as e:
        print(f"Error sorting artifacts: Missing key {e}")
    except Exception as e:
        print(f"Unexpected error in artifact sorter: {e}")
    print("\nTesting mage filter...")
    try:
        min_power = 80
        valid_mages = power_filter(mages, min_power)
        print(f"Valid mages with minimum power of {min_power}:")
        for mage in valid_mages:
            print(f"- {mage['name']} ({mage['power']} power)")
    except KeyError as e:
        print(f"Error filtering mages: Missing key {e}")
    except Exception as e:
        print(f"Unexpected error in filtering mages: {e}")
    print("\nTesting spell transformer...")
    try:
        transformed_spells = spell_transformer(spells)
        print(" ".join(transformed_spells))
    except Exception as e:
        print(f"Error transforming spells: {e}")
    print("\nTesting mage stats...")
    try:
        stats = mage_stats(mages)
        for stat, val in stats.items():
            print(f"{stat}: {val}")
    except KeyError as e:
        print(f"Error calculating stats: Missing key {e}")
    except Exception as e:
        print(f"Unexpected error in mage stats: {e}")


if __name__ == "__main__":
    main()
