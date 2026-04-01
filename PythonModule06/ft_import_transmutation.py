print("\n=== Import Transmutation Mastery ===\n")

import alchemy.elements
print("Method 1 - Full module import:")
print("alchemy.elements.create_fire():", alchemy.elements.create_fire())
print()

from alchemy.elements import create_fire
print("Method 2 - Specific function import:")
print("create_fire():", create_fire())
print()

from alchemy.potions import healing_potion as heal
print("Method 3 - Aliased import:")
print("heal():", heal())
print()

from alchemy.elements import create_fire, create_water
from alchemy.potions import strength_potion
print("Method 4 - Multiple imports:")
print("create_fire():", create_fire())
print("create_water():", create_water())
print("strength_potion():", strength_potion())
print()

print("All import transmutation methods mastered!")
