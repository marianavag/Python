def garden_operations(test_str: str) -> None:
    """Trigger different Python errors."""
    if test_str == "Value":
        int("abc")
    elif test_str == "ZeroDivision":
        1 / 0
    elif test_str == "FileNotFound":
        open("missing.txt")
    elif test_str == "Key":
        tmp = {}
        tmp["missing_plant"]


def test_error_types() -> None:
    """Demonstrate handling of different error types."""
    print("=== Garden Error Types Demo ===\n")
    tests = ["Value", "ZeroDivision", "FileNotFound", "Key"]
    for error_type in tests:
        try:
            print(f"Testing {error_type}Error...")
            garden_operations(error_type)
        except ValueError:
            print("Caught ValueError: invalid literal for int()\n")
        except ZeroDivisionError:
            print("Caught ZeroDivisionError: division by zero\n")
        except FileNotFoundError:
            print("Caught FileNotFoundError: No such file 'missing.txt'\n")
        except KeyError:
            print("Caught KeyError: 'missing\\_plant'\n")
    print("Testing multiple errors together...")
    try:
        garden_operations("Value")
    except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError):
        print("Caught an error, but program continues!\n")
    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
