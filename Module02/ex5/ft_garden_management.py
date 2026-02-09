class GardenError(Exception):
    """Base class for all garden errors."""
    pass


class PlantError(GardenError):
    """Raised when a plant has a problem."""
    pass


class WaterError(GardenError):
    """Raised when water has a problem."""
    pass


class GardenManager:
    """Manage plants, watering, and health checks in the garden."""
    def __init__(self) -> None:
        """Initialize the garden manager with an empty plant list."""
        self.plants = []

    def add_plant(self, plant_name: str) -> None:
        """Add a plant to the garden."""
        if not plant_name:
            raise PlantError("Plant name cannot be empty!")
        self.plants.append(plant_name)
        print(f"Added {plant_name} successfully")

    def water_plant(self, water_level: int) -> None:
        """Water all plants and ensure proper cleanup."""
        if water_level < 1:
            raise WaterError("Not enough water in tank")
        if water_level > 10:
            raise WaterError(f"Water level {water_level} is too high (max 10)")
        print("Opening watering system")
        try:
            for plant in self.plants:
                print(f"Watering {plant} - success")
        finally:
            print("Closing watering system (cleanup)")

    def check_plant_health(self, plant_name: str, water_level: int,
                           sunlight_hours: int) -> str:
        """Check plant health and validate growing conditions."""
        if not plant_name:
            raise PlantError("Plant name cannot be empty!")
        if water_level > 10:
            raise WaterError(f"Water level {water_level} is too high (max 10)")
        if water_level < 1:
            raise WaterError(f"Water level {water_level} is too low (min 1)")
        if sunlight_hours > 12:
            raise PlantError(f"Sunlight hours {sunlight_hours} "
                             f"is too high (max 12)")
        if sunlight_hours < 2:
            raise PlantError(f"Sunlight hours {sunlight_hours} "
                             f"is too low (min 2)")
        return (f"{plant_name}: healthy (water: {water_level}, "
                f"sun: {sunlight_hours})")


def test_garden_management() -> None:
    """Demonstrate garden management and error handling."""
    print("=== Garden Management System ===")
    manager = GardenManager()
    print("\nAdding plants to garden...")
    for plant_name in ["tomato", "lettuce", ""]:
        try:
            manager.add_plant(plant_name)
        except PlantError as e:
            print(f"Error adding plant: {e}")
    print("\nWatering plants...")
    try:
        manager.water_plant(5)
    except WaterError as e:
        print(f"Error watering plant: {e}")
    print("\nChecking plant health...")
    plants_to_check = [("tomato", 5, 8), ("lettuce", 15, 8)]
    for plant_name, water_level, sunlight_hours in plants_to_check:
        try:
            check = manager.check_plant_health(plant_name, water_level,
                                               sunlight_hours)
            print(check)
        except GardenError as e:
            print(f"Error checking {plant_name}: {e}")
    print("\nTesting error recovery...")
    try:
        manager.water_plant(0)
    except GardenError as e:
        print(f"Caught GardenError: {e}")
        print("System recovered and continuing...")
    print("\nGarden management system test complete!")


if __name__ == "__main__":
    test_garden_management()
