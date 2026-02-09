def water_plants(plant_list: list) -> None:
    """Water plants and always clean up."""
    print("Opening watering system")
    try:
        for plant in plant_list:
            if plant is None:
                raise ValueError("Cannot water None - invalid plant!")
            print(f"Watering {plant}")
    except ValueError:
        print("Error: Cannot water None - invalid plant!")
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system() -> None:
    """Demonstrate finally block behavior."""
    print("=== Garden Watering System ===\n")
    print("Testing normal watering...")
    test1 = ["tomato", "lettuce", "carrots"]
    water_plants(test1)
    print("Watering completed successfully!\n")
    print("Testing with error...")
    test2 = ["tomato", None]
    water_plants(test2)
    print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
