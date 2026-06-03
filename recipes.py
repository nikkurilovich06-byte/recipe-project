import copy

class Ingredient:
    def __init__ (self,name: str, quantity: float, unit: str):
        self.name = name
        self.quantity = quantity
        self.unit = unit

    @property
    def quantity(self)->float:
        return self._quantity

    @quantity.setter
    def quantity(self, value: float) -> None:
        if value<=0.0:
            raise ValueError("Количество должно быть положительным")
        self._quantity=float(value)
    
    def __str__(self) -> str:
        return f'{self.name}: {self.quantity} {self.unit}'

    def __repr__(self) -> str:
        return f"Ingredient('{self.name}',{self.quantity},'{self.unit}')"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Ingredient):
            return NotImplemented
        return self.name==other.name and self.unit==other.unit



class Recipe:
    def __init__(self, title: str, ingredients: list[Ingredient]):
        self.title = title
        self.ingredients = ingredients
    
    def add_ingredient(self, ingredient: Ingredient) -> None:
        for recipe_ingredient in self.ingredients:
            if recipe_ingredient==ingredient:
                recipe_ingredient.quantity +=ingredient.quantity
                return
        self.ingredients.append(ingredient)
        return 
    
    @staticmethod
    def is_valid_ratio(ratio) -> bool:
        return ratio>0
    
    def scale(self, ratio: float) -> Recipe:
        new_ingredients = []
        for ingredient in self.ingredients:
            new_ingredients.append(Ingredient(ingredient.name, ingredient.quantity * ratio, ingredient.unit))
        return Recipe(self.title, new_ingredients)
    
    def __len__(self) -> int:
        return len(self.ingredients)
    
    def __str__(self) -> str:
        output = self.title
        for ingredient in self.ingredients:
             output += '\n'
             output += f"{ingredient.name}: {ingredient.quantity} {ingredient.unit}"
        return output


'''
if __name__ == "__main__":
    muka=Ingredient("Мука",500,"г")
    eggs = Ingredient("Яйцо", 200, "г")
    cheese = Ingredient("Сыр", 300, "г")
    water = Ingredient("Вода", 100, "мл")
    cheese2 = Ingredient("Сыр", 400, "г")
    pizza_ingredients = [muka, eggs, cheese]
    pizza=Recipe("Пицца", pizza_ingredients)

    print(Recipe.is_valid_ratio(-10))
    print(pizza)
    pizza.add_ingredient(water)
    print(pizza)
    pizza.add_ingredient(cheese2)
    print(pizza)

    print(pizza.scale(2))
    print(len(pizza))
'''   


