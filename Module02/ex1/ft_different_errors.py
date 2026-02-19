def garden_operations() -> None:
    """Trigger different Python errors."""
    print("Testing ValueError...")
    try:
        int("abc")
    except ValueError as e:
        print(f"Caught ValueError: {e}\n")
    print("Testing ZeroDivisionError...")
    try:
        1/0
    except ZeroDivisionError as e:
        print(f"Caught ZeroDivisionError: {e}\n")
    print("Testing FileNotFoundError...")
    try:
        test3 = open("missing.txt")
        print(f"Testing {test3}Error...")
    except FileNotFoundError as e:
        print(f"Caught FileNotFoundError: {e}\n")
    print("Testing KeyError...")
    try:
        test4 = {}
        test4["missing_plant"]
        print(f"Testing {test4}Error...")
    except KeyError as e:
        print(f"Caught KeyError: {e}\n")
    print("Testing multiple errors together...")


def test_error_types() -> None:
    """Demonstrate handling of different error types."""
    print("=== Garden Error Types Demo ===\n")
    garden_operations()
    print("Caught an error, but program continues!\n")
    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
