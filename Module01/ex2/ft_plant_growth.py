class Plant:
    """Blueprint representing a plant in the garden."""
    def __init__(self, name: str, height: int, agedays: int) -> None:
        """Initialize plant name, height, and age."""
        self.name = name
        self.height = height
        self.agedays = agedays

    def grow(self, centimeters: int) -> None:
        """Increase the plant's height by the given number of centimeters."""
        self.height += centimeters

    def age(self, days: int) -> None:
        """Increase the plant's age by the given number of days."""
        self.agedays += days

    def get_info(self) -> str:
        """Return the plant's current status."""
        return (f"{self.name}: {self.height}cm, {self.agedays} days old")


def ft_plant_growth() -> None:
    """Simulate one week of plant growth and displays the progress."""
    rose = Plant("Rose", 25, 30)
    initial_height = rose.height
    for day in range(1, 8):
        if day == 1 or day == 7:
            print(f"=== Day {day} ===")
            print(rose.get_info())
        if day < 7:
            rose.grow(1)
            rose.age(1)
    growth_total = rose.height - initial_height
    print(f"Growth this week: +{growth_total}cm")


if __name__ == "__main__":
    ft_plant_growth()
