class Plant:
    """Blueprint representing a plant in the garden."""
    def __init__(self, name: str, height: int, age: int) -> None:
        """Initialize plant name, height, and age."""
        self.name = name
        self.height = height
        self.age = age

    def display_info(self) -> None:
        """Print the plant's data in a specific format."""
        print(f"{self.name}: {self.height}cm, {self.age} days old")


def ft_garden_data() -> None:
    """Manage and displays the garden data."""
    print("=== Garden Plant Registry ===")
    rose = Plant("Rose", 25, 30)
    sunflower = Plant("Sunflower", 80, 45)
    cactus = Plant("Cactus", 15, 120)
    my_plants = [rose, sunflower, cactus]
    for plant in my_plants:
        plant.display_info()


if __name__ == "__main__":
    ft_garden_data()
