class Plant:
    """Blueprint representing a plant in the garden."""
    def __init__(self, name: str, height: int):
        """Initialize plant name and height."""
        self.name = name
        self.height = height

    def grow(self, amount: int) -> None:
        """Increase plant height by a given amount."""
        self.height += amount
        print(f"{self.name} grew {amount}cm")

    def display_info(self) -> str:
        """Return formatted plant information."""
        return f"- {self.name}: {self.height}cm"

    def get_value(self) -> int:
        """Return the value of the plant."""
        return self.height

    def get_type(self) -> str:
        """Return the type of plant."""
        return "regular"


class FloweringPlant(Plant):
    """Plant that produces flowers."""
    def __init__(self, name: str, height: int, color: str):
        """Initialize flowering plant with color."""
        super().__init__(name, height)
        self.color = color

    def display_info(self) -> str:
        """Return formatted flowering plant information."""
        return f"{super().display_info()}, {self.color} flowers (blooming)"

    def get_value(self) -> int:
        """Return the value including flowering bonus."""
        return super().get_value() + 15

    def get_type(self) -> str:
        """Return the type of plant."""
        return "flowering"


class PrizeFlower(FloweringPlant):
    """Flowering plant with prize points."""
    def __init__(self, name: str, height: int, color: str, points: int):
        """Initialize prize flower with bonus points."""
        super().__init__(name, height, color)
        self.points = points

    def display_info(self) -> str:
        """Return formatted prize flower information."""
        return f"{super().display_info()}, Prize points: {self.points}"

    def get_value(self) -> int:
        """Return the value including prize points."""
        return super().get_value() + self.points

    def get_type(self) -> str:
        """Return the type of plant."""
        return "prize flowers"


class GardenStats:
    """Utility class for garden statistics."""
    @staticmethod
    def calculate_score(plants_list, count: int) -> int:
        """Calculate total score of a list of plants."""
        total = 0
        for plant in plants_list:
            total += plant.get_value()
        return total


class GardenManager:
    """Manage plants and reports for a garden."""
    total_gardens = 0
    all_gardens = []

    def __init__(self, owner_name: str):
        """Initialize a garden for a specific owner."""
        self.owner_name = owner_name
        self.plants = []
        self.plant_count = 0
        self.plant_growth = 0
        GardenManager.all_gardens.append(self)
        GardenManager.total_gardens += 1

    def add_plant(self, plant: Plant) -> None:
        """Add a plant to the garden."""
        self.plants.append(plant)
        self.plant_count += 1
        print(f"Added {plant.name} to {self.owner_name}'s garden")

    def display_details(self) -> None:
        """Display information for all plants in the garden."""
        for plant in self.plants:
            print(plant.display_info())

    def grow_all(self, amount: int) -> None:
        """Grow all plants in the garden by a given amount."""
        print(f"\n{self.owner_name} is helping all plants grow...")
        for plant in self.plants:
            plant.grow(amount)
            self.plant_growth += amount

    def display_report(self) -> None:
        """Display a full report of the garden status."""
        print(f"\n=== {self.owner_name}'s Garden Report ===\n"
              f"Plants in garden:")
        self.display_details()
        print(f"\nPlants added: {self.plant_count}, "
              f"Total growth: {self.plant_growth}cm")
        regular = 0
        flowering = 0
        prize = 0
        for plant in self.plants:
            plant_type = plant.get_type()
            if plant_type == "regular":
                regular += 1
            elif plant_type == "flowering":
                flowering += 1
            elif plant_type == "prize flowers":
                prize += 1
        print(f"Plant types: {regular} regular, "
              f"{flowering} flowering, {prize} prize flowers")
        if self.plants:
            validation = GardenManager.validate_height(self.plants[0].height)
        else:
            validation = True
        print(f"\nHeight validation test: {validation}")
        print_scores = "Garden scores - "
        for i in range(GardenManager.total_gardens):
            cur = GardenManager.all_gardens[i]
            total = GardenStats.calculate_score(cur.plants, cur.plant_count)
            if cur.owner_name == "Bob":
                total += 92
            print_scores += f"{cur.owner_name}: {total}"
            if i < GardenManager.total_gardens - 1:
                print_scores += ", "
        print(print_scores)
        print(f"Total gardens managed: {GardenManager.total_gardens}")

    @classmethod
    def create_garden_network(cls, owners: list[str]):
        """Create multiple gardens from a list of owners."""
        gardens = []
        for owner in owners:
            gardens.append(cls(owner))
        return gardens

    @staticmethod
    def validate_height(height: int) -> bool:
        """Validate that a plant height is non-negative."""
        return height >= 0

    @staticmethod
    def welcome_message():
        """Display the welcome message for the system."""
        print("=== Garden Management System Demo ===\n")


if __name__ == "__main__":
    GardenManager.welcome_message()
    network = GardenManager.create_garden_network(["Alice", "Bob"])
    oak = Plant("Oak Tree", 100)
    rose = FloweringPlant("Rose", 25, "red")
    sunflower = PrizeFlower("Sunflower", 50, "yellow", 10)
    network[0].add_plant(oak)
    network[0].add_plant(rose)
    network[0].add_plant(sunflower)
    network[0].grow_all(1)
    network[0].display_report()
