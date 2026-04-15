from abc import ABC, abstractmethod
from ex0.creature_factory import Creature, CreatureFactory


class HealCapability(ABC):
    @abstractmethod
    def heal(self, target: str) -> str:
        pass


class TransformCapability(ABC):
    def __init__(self) -> None:
        self.is_transformed: bool = False

    @abstractmethod
    def transform(self) -> str:
        pass

    @abstractmethod
    def revert(self) -> str:
        pass


class Sproutling(Creature, HealCapability):
    def __init__(self) -> None:
        super().__init__("Sproutling", "Grass")

    def attack(self) -> str:
        return f"{self.c_name} uses Vine Whip!"

    def heal(self, target: str) -> str:
        return f"{self.c_name} heals {target} for a small amount"


class Bloomelle(Creature, HealCapability):
    def __init__(self) -> None:
        super().__init__("Bloomelle", "Grass/Fairy")

    def attack(self) -> str:
        return f"{self.c_name} uses Petal Dance!"

    def heal(self, target: str) -> str:
        return f"{self.c_name} heals {target} for a large amount"


class Shiftling(Creature, TransformCapability):
    def __init__(self) -> None:
        super().__init__("Shiftling", "Normal")
        TransformCapability.__init__(self)

    def attack(self) -> str:
        if self.is_transformed:
            return f"{self.c_name} performs a boosted strike!"
        return f"{self.c_name} attacks normally."

    def transform(self) -> str:
        self.is_transformed = True
        return f"{self.c_name} shifts into a sharper form!"

    def revert(self) -> str:
        self.is_transformed = False
        return f"{self.c_name} returns to normal."


class Morphagon(Creature, TransformCapability):
    def __init__(self) -> None:
        super().__init__("Morphagon", "Normal/Dragon")
        TransformCapability.__init__(self)

    def attack(self) -> str:
        if self.is_transformed:
            return f"{self.c_name} unleashes a devastating morph strike!"
        return f"{self.c_name} attacks normally."

    def transform(self) -> str:
        self.is_transformed = True
        return f"{self.c_name} morphs into a dragonic battle form!"

    def revert(self) -> str:
        return f"{self.c_name} stabilizes its form."


class HealingCreatureFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return Sproutling()

    def create_evolved(self) -> Creature:
        return Bloomelle()


class TransformCreatureFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return Shiftling()

    def create_evolved(self) -> Creature:
        return Morphagon()
