def validate_ingredients(ingredients: str) -> str:
    valid_ingredients = {"fire", "water", "earth", "air"}
    words = ingredients.split()
    for word in words:
        if word not in valid_ingredients:
            return f"{ingredients} - INVALID"
        return f"{ingredients} - VALID"
    return "[ingredients] - VALID" or "[ingredients] - INVALID"
