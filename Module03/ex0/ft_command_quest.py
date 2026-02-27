import sys


def ft_command_quest() -> None:
    """Display command-line arguments in a user-friendly way."""
    print("=== Command Quest ===")
    if len(sys.argv) < 2:
        print("No arguments provided!")
        print(f"Program name: {sys.argv[0]}")
        print(f"Total arguments: {len(sys.argv)}")
    else:
        print(f"Program name: {sys.argv[0]}")
        user_args = sys.argv[1:]
        print(f"Arguments received: {len(user_args)}")
        count = 1
        for arg in user_args:
            print(f"Argument {count}: {arg}")
            count += 1
        print(f"Total arguments: {len(sys.argv)}\n")


if __name__ == "__main__":
    ft_command_quest()
