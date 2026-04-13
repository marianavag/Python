from abc import ABC, abstractmethod
from ex0.creature_factory import Creature
from ex1 import HealCapability, TransformCapability


class InvalidStrategyError(Exception):
    pass


class BattleStrategy(ABC):
    @abstractmethod
    def act(self, creature: Creature) -> str:
        pass

    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        pass


class NormalStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return True

    def act(self, creature: Creature) -> str:
        print(creature.attack())


class AggressiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, TransformCapability)

    def act(self, creature: Creature) -> str:
        if not self.is_valid(creature):
            raise InvalidStrategyError(f"Invalid Creature '{creature.c_name}' "
                                       f"for this aggressive strategy")
        results = [
                creature.transform(),
                creature.attack(),
                creature.revert()
            ]
        return "\n".join(results)


class DefensiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, HealCapability)

    def act(self, creature: Creature) -> str:
        if not self.is_valid(creature):
            raise InvalidStrategyError(f"Invalid Creature '{creature.c_name}' "
                                       f"for this defensive strategy")
        results = [
            creature.attack(),
            creature.heal("itself")
        ]
        return "\n".join(results)
