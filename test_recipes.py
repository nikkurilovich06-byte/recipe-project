import pytest
from recipes import Ingredient, Recipe, ShoppingList, DietaryRecipe

def test_initialize_ingredient():
    ingredient1=Ingredient("Мука", 500, "г")
    assert ingredient1.name == "Мука"
    assert ingredient1.quantity == 500.0
    assert ingredient1.unit == "г"

def test_ingredient_str():
    ingredient1= Ingredient("Мука", 500, "г")
    assert str(ingredient1)=="Мука: 500.0 г"

def test_same_ingredients_are_equal_with_same_name_and_unit():
    ingredient1= Ingredient("Мука", 500, "г")
    ingredient2= Ingredient("Мука", 200, "г")
    assert ingredient1==ingredient2

def test_ingredients_are_not_equal_with_different_names():
    ingredient1= Ingredient("Мука", 500, "г")
    ingredient2= Ingredient("Сыр", 500, "г")
    assert ingredient1!=ingredient2

def test_ingredients_are_not_equal_with_different_units():
    ingredient1= Ingredient("Мука", 500, "кг")
    ingredient2= Ingredient("Мука", 500, "г")
    assert ingredient1!=ingredient2



def test_recipe_creation():
    ingredient1= Ingredient("Мука", 500, "г")
    ingredient2= Ingredient("Сыр", 300, "г")
    recipe1 = Recipe("Пицца", [ingredient1, ingredient2])
    assert recipe1.title == "Пицца"
    assert recipe1.ingredients[0].name == "Мука"
    assert recipe1.ingredients[0].quantity == 500.0
    assert recipe1.ingredients[0].unit == "г"
    assert recipe1.ingredients[1].name == "Сыр"
    assert recipe1.ingredients[1].quantity == 300.0
    assert recipe1.ingredients[1].unit == "г"

def test_add_new_ingredient():
    ingredient1= Ingredient("Мука", 500, "г")
    ingredient2= Ingredient("Сыр", 300, "г")
    recipe1 = Recipe("Пицца", [ingredient1, ingredient2])
    ingredient3 = Ingredient("Соль", 50, "г")
    recipe1.add_ingredient(ingredient3)
    assert ingredient3 in recipe1.ingredients
    assert len(recipe1.ingredients)==3

def test_add_existing_ingredient():
    ingredient1= Ingredient("Мука", 500, "г")
    ingredient2= Ingredient("Сыр", 300, "г")
    recipe1 = Recipe("Пицца", [ingredient1, ingredient2])
    ingredient3 = Ingredient("Мука", 100, "г")
    recipe1.add_ingredient(ingredient3)
    new_ingredient = recipe1.ingredients[0]
    assert new_ingredient.name == "Мука"
    assert new_ingredient.quantity == 600
    assert new_ingredient.unit == "г"
    assert len(recipe1.ingredients)==2

def test_scale_makes_new_object():
    ingredient1= Ingredient("Мука", 500, "г")
    ingredient2= Ingredient("Сыр", 300, "г")
    recipe1 = Recipe("Пицца", [ingredient1, ingredient2])
    recipe2=recipe1.scale(2)
    assert recipe2 is not recipe1
    assert isinstance(recipe2, Recipe)
    assert recipe1.ingredients[0].quantity == 500.0
    assert recipe1.ingredients[1].quantity == 300.0


def test_scale_multiply_quantity_of_ingredients():
    ingredient1= Ingredient("Мука", 500, "г")
    ingredient2= Ingredient("Сыр", 300, "г")
    recipe1 = Recipe("Пицца", [ingredient1, ingredient2])
    recipe2=recipe1.scale(2)
    assert recipe2.ingredients[0].quantity == 2*500.0
    assert recipe2.ingredients[1].quantity == 2*300.0

def test_ratio_cannot_be_zero_or_lower():
    ingredient1= Ingredient("Мука", 500, "г")
    ingredient2= Ingredient("Сыр", 300, "г")
    recipe1 = Recipe("Пицца", [ingredient1, ingredient2])

    with pytest.raises(ValueError):
        recipe1.scale(0)
    with pytest.raises(ValueError):
        recipe1.scale(-1)


def test_len_returns_quantity_of_unique_ingredients():
    ingredient1= Ingredient("Мука", 500, "г")
    ingredient2= Ingredient("Сыр", 300, "г")
    recipe1 = Recipe("Пицца", [ingredient1, ingredient2])
    ingredient3 = Ingredient("Мука", 100, "г")
    recipe1.add_ingredient(ingredient3)
    assert len(recipe1) == 2