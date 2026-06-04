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


