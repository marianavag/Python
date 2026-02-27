import math


def get_distance(ori: tuple[int, int, int], pos: tuple[int, int, int],
                 decimal: int) -> None:
    """Print the Euclidean distance between two 3D points."""
    distance = math.sqrt(
            (pos[0]-ori[0])**2 +
            (pos[1]-ori[1])**2 +
            (pos[2]-ori[2])**2
        )
    print(f"Distance between {ori} and {pos}: {distance:.{decimal}f}\n")


def parsing_args(string: str) -> tuple[int, int, int] | None:
    """Parse a string into a 3D coordinate tuple or return None on error."""
    parsed_pos = string.split(",")
    temp_list = []
    for char in parsed_pos:
        try:
            temp_list.append(int(char))
        except ValueError as e:
            first_arg, *rest = e.args
            print(f'Parsing invalid coordinates: "{string}"')
            print(f"Error parsing coordinates: {first_arg}")
            print(f'Error details - Type: ValueError, Args: {e.args}\n')
            if rest:
                print(f"Other args: {rest}")
            return None
    pos = tuple(temp_list)
    print(f"Parsed position: {pos}")
    return pos


def ft_coordinate_system() -> None:
    """Demonstrate 3D coordinates, distance calculation, and parsing."""
    print("=== Game Coordinate System ===\n")
    ori = (0, 0, 0)
    ex1 = (10, 20, 5)
    print(f"Position created: {ex1}")
    get_distance(ori, ex1, decimal=2)
    ex2 = "3,4,0"
    print(f'Parsing coordinates: "{ex2}"')
    parsed_ex2 = parsing_args(ex2)
    if parsed_ex2:
        get_distance(ori, parsed_ex2, decimal=1)
    ex3 = "abc,def,ghi"
    parsing_args(ex3)
    if parsed_ex2:
        print("Unpacking demonstration:")
        x, y, z = parsed_ex2
        print(f"Player at x={x}, y={y}, z={z}")
        print(f"Coordinates: X={x}, Y={y}, Z={z}")


if __name__ == "__main__":
    ft_coordinate_system()
