class Plant:
    """Blueprint representing a plant in the garden."""
    def __init__(self, name: str, height: int, agedays: int) -> None:
        """Initialize plant name, height, and age."""
        self.name = name
        self.height = height
        self.agedays = agedays

    def get_info(self) -> str:
        """Return the plant's current status."""
        return (f"Created: {self.name} ({self.height}cm, {self.agedays} days)")


def ft_plant_factory():
    """Instantiate plants from a predefined list and prints their status."""
    total_plants = 0
    print("=== Plant Factory Output ===")
    p_data = [
        ("Rose", 25, 30),
        ("Oak", 200, 365),
        ("Cactus", 5, 90),
        ("Sunflower", 80, 45),
        ("Fern", 15, 120)
    ]
    plants = [Plant(name, height, agedays) for name, height, agedays in p_data]
    for p in plants:
        print(p.get_info())
        total_plants += 1
    print(f"\nTotal plants created: {total_plants}")


if __name__ == "__main__":
    ft_plant_factory()
