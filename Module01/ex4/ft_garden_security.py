class SecurePlant:
    """A plant class with protected attributes and validated setters."""
    def __init__(self, name: str, height: int, agedays: int) -> None:
        """Initialize plant name, height, and age."""
        self.name = name
        self.__height = height
        self.__agedays = agedays

    def set_height(self, value: int) -> None:
        """Update height if the value is non-negative."""
        if value < 0:
            print(f"\nInvalid operation attempted: height {value}cm [REJECTED]"
                  f"\nSecurity: Negative height rejected\n")
        else:
            self.__height = value
            print(f"Height updated: {self.__height}cm [OK]")

    def set_age(self, value: int) -> None:
        """Update age if the value is non-negative."""
        if value < 0:
            print(f"\nInvalid operation attempted: age {value} days [REJECTED]"
                  f"\nSecurity: Negative age rejected\n")
        else:
            self.__agedays = value
            print(f"Age updated: {self.__agedays} days [OK]")

    def get_height(self) -> int:
        """Return the current height of the plant."""
        return self.__height

    def get_age(self) -> int:
        """Return the current age of the plant."""
        return self.__agedays


def ft_garden_security() -> None:
    """Test the security system by attempting valid and invalid updates."""
    print("=== Garden Security System ===")
    rose = SecurePlant("Rose", 25, 30)
    print(f"Plant created: {rose.name}")
    rose.set_height(25)
    rose.set_age(30)
    rose.set_height(-5)
    print(f"Current plant: {rose.name} "
          f"({rose.get_height()}cm, {rose.get_age()} days)")


if __name__ == "__main__":
    ft_garden_security()
