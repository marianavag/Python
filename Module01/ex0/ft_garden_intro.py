#!/usr/bin/env python3

def ft_garden_intro() -> None:
    """
    Display information about a plant.
    """
    print("=== Welcome to My Garden ===")
    plant_name: str = "Rose"
    plant_height: int = 25
    plant_age: int = 30
    print(f"Plant: {plant_name}")
    print(f"Height: {plant_height}cm")
    print(f"Age: {plant_age} days")
    print("\n=== End of Program ===")


if __name__ == "__main__":
    ft_garden_intro()
