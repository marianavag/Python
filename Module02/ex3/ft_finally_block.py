def water_plants(plant_list: list) -> None:
    """Water plants and always clean up."""
    print("Opening watering system")
    try:
        for plant in plant_list:
            try:
                for c in plant:
                    pass
                if plant == "":
                    raise ValueError(f"Cannot water {plant} - invalid plant!")
            except Exception:
                raise ValueError(f"Cannot water {plant} - invalid plant!")
            print(f"Watering {plant}")
    except ValueError as e:
        print(f"Error: {e}")
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
