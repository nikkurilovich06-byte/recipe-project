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
        return isinstance(ratio, (int, float)) and ratio > 0
    
    def scale(self, ratio: float) -> Recipe:
        if not Recipe.is_valid_ratio(ratio):
            raise ValueError("Коэффициент должен быть положительным")

        new_ingredients = []

        for ingredient in self.ingredients:
            new_ingredients.append(
                Ingredient(
                    ingredient.name,
                    ingredient.quantity * ratio,
                    ingredient.unit))

        return Recipe(self.title, new_ingredients)
    
    def __len__(self) -> int:
        return len(self.ingredients)
    
    def __str__(self) -> str:
        output = self.title
        for ingredient in self.ingredients:
             output += '\n'
             output += f"{ingredient.name}: {ingredient.quantity} {ingredient.unit}"
        return output


class ShoppingList:
    def __init__(self, _items: list[(Ingredient, str)] | None = None):
        self._items = _items if _items is not None else []
    
    def add_recipe(self, recipe: Recipe, portions: float) -> None:
        if portions <= 0:
            raise ValueError("Количество порций должно быть положительным")
        recipe = recipe.scale(portions)
        for recipe_ingredient in recipe.ingredients:
                self._items.append((recipe_ingredient, recipe.title))

    
    def remove_recipe(self, title: str) -> None:
        self._items = [item for item in self._items if item[1] != title] 

    def get_list(self)-> list[Ingredient]:
        shopping_list_ingredients_dict = {}
        for ingredient, title in self._items:
            key = (ingredient.name, ingredient.unit)
            if key in shopping_list_ingredients_dict:
                shopping_list_ingredients_dict[key] += ingredient.quantity
            else:
               shopping_list_ingredients_dict[key] = ingredient.quantity

        shopping_list_ingredients=[]
        for item in shopping_list_ingredients_dict:
            shopping_list_ingredients.append(Ingredient(item[0], shopping_list_ingredients_dict.get(item), item[1]))
        shopping_list_ingredients.sort(key=lambda ingredient: ingredient.name) #key sorting - https://docs.python.org/3/howto/sorting.html
        return shopping_list_ingredients    

    def __add__(self, other: ShoppingList) -> ShoppingList:
        new_list = ShoppingList()

        for ingredient, title in self._items:
            copied_ingredient = Ingredient(
                ingredient.name,
                ingredient.quantity,
                ingredient.unit
            )
            new_list._items.append((copied_ingredient, title))

        for ingredient, title in other._items:
            copied_ingredient = Ingredient(
                ingredient.name,
                ingredient.quantity,
                ingredient.unit
            )
            new_list._items.append((copied_ingredient, title))

        return new_list
    

class DietaryRecipe(Recipe):
    def __init__(self,title: str, diet_type: str, ingredients: list[Ingredient]|None=None):
        if ingredients is None:
            ingredients = []
        super().__init__(title, ingredients)
        self.diet_type=diet_type

    def scale(self, ratio:float) -> DietaryRecipe:
         recipe=super().scale(ratio)
         return DietaryRecipe(recipe.title, self.diet_type, recipe.ingredients)
    
    def __str__(self) -> str:
        return f"[{self.diet_type}] "+super().__str__()

