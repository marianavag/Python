def garden_operations(tests: str) -> None:
    """Trigger different Python errors."""
    try:
        if tests == "ValueError":
            int("abc")
        elif tests == "ZeroDivisionError":
            42 / 0
        elif tests == "FileNotFoundError":
            open("missing.txt")
        elif tests == "KeyError":
            test4 = {}
            test4["missing_plant"]
    except ValueError:
        print("Caught ValueError: invalid literal for int()\n")
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero\n")
    except FileNotFoundError:
        print("Caught FileNotFoundError: No such file 'missing.txt'\n")
    except KeyError:
        print("Caught KeyError: 'missing\\_plant'\n")
    try:
        if tests == "multiple":
            raise ValueError("Caught ValueError: invalid literal for int()\n")
    except (ValueError, ZeroDivisionError):
        print("Caught an error, but program continues!\n")


def test_error_types() -> None:
    """Demonstrate handling of different error types."""
    print("=== Garden Error Types Demo ===\n")
    print("Testing ValueError...")
    garden_operations("ValueError")
    print("Testing ZeroDivisionError...")
    garden_operations("ZeroDivisionError")
    print("Testing FileNotFoundError...")
    garden_operations("FileNotFoundError")
    print("Testing KeyError...")
    garden_operations("KeyError")
    print("Testing multiple errors together...")
    garden_operations("multiple")
    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
