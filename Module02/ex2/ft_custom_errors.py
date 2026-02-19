class GardenError(Exception):
    """Base class for all garden errors."""
    pass


class PlantError(GardenError):
    """Raised when a plant has a problem."""
    pass


class WaterError(GardenError):
    """Raised when water has a problem."""
    pass


def check_plant_health(status: str) -> None:
    """Check plant health and raise error if needed."""
    if status == "wilting":
        raise PlantError(f"The tomato plant is {status}!")
    else:
        print("Plant is probably healthy!\n")


def check_water_level(level: int) -> None:
    """Check water level and raise error if too low."""
    if level < 10:
        raise WaterError("Not enough water in the tank!")
    else:
        print("Enough water in the tank!\n")


def test_custom_errors() -> None:
    """Demonstrate custom garden error handling."""
    print("=== Custom Garden Errors Demo ===\n")
    print("Testing PlantError...")
    try:
        check_plant_health("wilting")
    except PlantError as e:
        print(f"Caught PlantError: {e}\n")
    print("Testing WaterError...")
    try:
        check_water_level(9)
    except WaterError as e:
        print(f"Caught WaterError: {e}\n")
    print("Testing catching all garden errors...")
    try:
        check_plant_health("wilting")
    except GardenError as e:
        print(f"Caught a garden error: {e}")
    try:
        check_water_level(9)
    except GardenError as e:
        print(f"Caught a garden error: {e}")
    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    test_custom_errors()
