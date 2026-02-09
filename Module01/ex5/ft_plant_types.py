class Plant:
    """Blueprint representing a plant in the garden."""
    def __init__(self, name: str, height: int, age: int) -> None:
        """Initialize plant name, height, and age."""
        self.name = name
        self.height = height
        self.age = age

    def display_base_info(self) -> None:
        """Print basic information about the plant."""
        print(f"{self.name} ({self.__class__.__name__}): "
              f"{self.height}cm, {self.age} days", end="")


class Flower(Plant):
    """Represents a flower plant."""
    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        """Initialize a flower with its color."""
        super().__init__(name, height, age)
        self.color = color

    def bloom(self) -> None:
        """Display a blooming message."""
        print(f"{self.name} is blooming beautifully!\n")

    def display_info(self) -> None:
        """Display flower information and bloom."""
        super().display_base_info()
        print(f", {self.color} color")
        self.bloom()


class Tree(Plant):
    """Represent a tree plant."""
    def __init__(self, name: str, height: int, age: int,
                 trunk_diameter: int) -> None:
        """Initialize a tree with trunk diameter."""
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        """Calculate and print shade area."""
        shade_area = (self.trunk_diameter * 3)//2 + 3
        print(f"{self.name} provides {shade_area} square meters of shade\n")

    def display_info(self) -> None:
        """Display tree information and shade."""
        super().display_base_info()
        print(f", {self.trunk_diameter}cm diameter")
        self.produce_shade()


class Vegetable(Plant):
    """Represent a vegetable plant."""
    def __init__(self, name: str, height: int, age: int, harvest_season: str,
                 nutritional_value: str) -> None:
        """Initialize a vegetable with harvest data."""
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def display_info(self) -> None:
        """Display vegetable information and nutrition."""
        super().display_base_info()
        print(f", {self.harvest_season} harvest")
        print(f"{self.name} is rich in vitamin {self.nutritional_value}")


def ft_plant_types() -> None:
    """Display all plant types in the garden."""
    print("=== Garden Plant Types ===\n")
    garden = [
        Flower("Rose", 25, 30, "red"),
        Flower("Tulip", 15, 20, "yellow"),
        Tree("Oak", 500, 1825, 50),
        Tree("Pine", 300, 1000, 40),
        Vegetable("Tomato", 80, 90, "summer", "C"),
        Vegetable("Carrot", 30, 60, "autumn", "A")
    ]
    first_plant = True
    for plant in garden:
        if not first_plant:
            print()
        plant.display_info()
        first_plant = False


if __name__ == "__main__":
    ft_plant_types()
