def check_temperature(temp_str: str) -> int | None:
    """Check if temperature is valid and safe for plants."""
    try:
        temp = int(temp_str)
        if 0 <= temp <= 40:
            print(f"Temperature {temp}°C is perfect for plants!")
            return temp
        elif temp < 0:
            raise ValueError(f"{temp}°C is too cold for plants (min 0°C)")
        elif temp > 40:
            raise ValueError(f"{temp}°C is too hot for plants (max 40°C)")
    except Exception as e:
        print(f"Error: {e}")


def test_temperature_input() -> None:
    """Run predefined temperature tests and print the results."""
    print("=== Garden Temperature Checker ===\n")
    tests = ["25", "abc", "100", "-50"]
    for i in tests:
        print(f"Testing temperature: {i}")
        check_temperature(i)
        print()
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature_input()
