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





def test_add_recipe_to_shopping_list():
    ingredient1= Ingredient("Мука", 500, "г")
    ingredient2= Ingredient("Сыр", 300, "г")
    recipe1 = Recipe("Пицца", [ingredient1, ingredient2])
    ingredient3= Ingredient("Вода", 500, "мл")
    ingredient4= Ingredient("Мука", 300, "г")
    recipe2 = Recipe("Хлебная кайфуля", [ingredient3, ingredient4])

    shopping_list1 = ShoppingList([(ingredient1, recipe1.title), (ingredient2, recipe1.title)])
    shopping_list1.add_recipe(recipe2, 3)
    result = shopping_list1.get_list()
    
    assert len(shopping_list1._items)==4
    assert len(result)==3
    ingredient1_from_list = next(ingredient for ingredient in result if ingredient.name == "Мука") #next - https://docs.python.org/3/library/functions.html#next
    ingredient2_from_list = next(ingredient for ingredient in result if ingredient.name == "Сыр") #next - https://docs.python.org/3/library/functions.html#next
    ingredient3_from_list = next(ingredient for ingredient in result if ingredient.name == "Вода") #next - https://docs.python.org/3/library/functions.html#next

    assert ingredient1_from_list.quantity == 1400.0
    assert ingredient1_from_list.unit == "г"

    assert ingredient2_from_list.quantity == 300.0
    assert ingredient2_from_list.unit == "г"

    assert ingredient3_from_list.quantity == 1500.0
    assert ingredient3_from_list.unit == "мл"


def test_portion_lower_zero_raises_error():
    recipe1 = Recipe("Пицца", [Ingredient("Мука", 500, "г")])
    shopping_list1 = ShoppingList()

    with pytest.raises(ValueError):
        shopping_list1.add_recipe(recipe1, 0)
    with pytest.raises(ValueError):
        shopping_list1.add_recipe(recipe1, -1)


def test_remove_existing_ingredients_by_removing_recipe():
    ingredient1= Ingredient("Мука", 500, "г")
    ingredient2= Ingredient("Сыр", 300, "г")
    recipe1 = Recipe("Пицца", [ingredient1, ingredient2])
    ingredient3= Ingredient("Вода", 500, "мл")
    ingredient4= Ingredient("Мука", 300, "г")
    recipe2 = Recipe("Хлебная кайфуля", [ingredient3, ingredient4])

    shopping_list1 = ShoppingList()
    shopping_list1.add_recipe(recipe1, 1)
    shopping_list1.add_recipe(recipe2, 1)

    shopping_list1.remove_recipe("Хлебная кайфуля")

    result = shopping_list1.get_list()

    assert len(result) == 2

    flour = next(ingredient for ingredient in result if ingredient.name == "Мука")
    cheese = next(ingredient for ingredient in result if ingredient.name == "Сыр")

    assert flour.quantity == 500.0
    assert cheese.quantity == 300.0

def test_remove_recipe_with_unknown_title_does_nothing():
    ingredient1= Ingredient("Мука", 500, "г")
    ingredient2= Ingredient("Сыр", 300, "г")
    recipe1 = Recipe("Пицца", [ingredient1, ingredient2])

    shopping_list1 = ShoppingList()
    shopping_list1.add_recipe(recipe1, 1)
    
    shopping_list1.remove_recipe("Каша")
    result=shopping_list1.get_list()
    assert len(result)==2
    assert ingredient1 in result
    assert ingredient2 in result

def test_get_list_same_ingredients_sums():
    ingredient1= Ingredient("Мука", 500, "г")
    ingredient2= Ingredient("Сыр", 300, "г")
    recipe1 = Recipe("Пицца", [ingredient1, ingredient2])
    ingredient3= Ingredient("Вода", 500, "мл")
    ingredient4= Ingredient("Мука", 300, "г")
    recipe2 = Recipe("Хлебная кайфуля", [ingredient3, ingredient4])

    shopping_list1 = ShoppingList()
    shopping_list1.add_recipe(recipe1, 1)
    shopping_list1.add_recipe(recipe2, 1)
    result = shopping_list1.get_list()

    assert len(result)==3
    flour = next(ingredient for ingredient in result if ingredient.name == "Мука") #next - https://docs.python.org/3/library/functions.html#next
    assert flour.quantity == 800.0
    assert flour.unit == "г"

def test_get_list_sorted_by_name_of_ingredient():
        pizza = Recipe("Пицца",[
            Ingredient("Мука", 500, "г"),
            Ingredient("Сыр", 300, "г"),
            Ingredient("Вода", 100, "мл"),])
        shopping_list = ShoppingList()
        shopping_list.add_recipe(pizza, 1)
        result = shopping_list.get_list()
        assert result[0].name == "Вода"
        assert result[1].name == "Мука"
        assert result[2].name == "Сыр"

def test_add_return_new_list():
    ingredient1= Ingredient("Мука", 500, "г")
    ingredient2= Ingredient("Сыр", 300, "г")
    recipe1 = Recipe("Пицца", [ingredient1, ingredient2])
    ingredient3= Ingredient("Вода", 500, "мл")
    ingredient4= Ingredient("Мука", 300, "г")
    recipe2 = Recipe("Хлебная кайфуля", [ingredient3, ingredient4])

    shopping_list1 = ShoppingList()
    shopping_list1.add_recipe(recipe1, 1)
    shopping_list2 = ShoppingList()
    shopping_list2.add_recipe(recipe2, 1)

    new_shopping_list = shopping_list1 + shopping_list2

    result = new_shopping_list.get_list()

    assert isinstance(new_shopping_list, ShoppingList)
    assert new_shopping_list is not shopping_list1
    assert new_shopping_list is not shopping_list2
    assert len(result) == 3

    flour = next(ingredient for ingredient in result if ingredient.name == "Мука") #next - https://docs.python.org/3/library/functions.html#next
    water = next(ingredient for ingredient in result if ingredient.name == "Вода")#next - https://docs.python.org/3/library/functions.html#next
    cheese = next(ingredient for ingredient in result if ingredient.name == "Сыр")#next - https://docs.python.org/3/library/functions.html#next
    assert flour.quantity == 800.0
    assert water.quantity == 500.0
    assert cheese.quantity == 300.0

def test_add_does_not_change_original_shopping_lists():
    ingredient1= Ingredient("Мука", 500, "г")
    ingredient2= Ingredient("Сыр", 300, "г")
    recipe1 = Recipe("Пицца", [ingredient1, ingredient2])
    ingredient3= Ingredient("Вода", 500, "мл")
    ingredient4= Ingredient("Мука", 300, "г")
    recipe2 = Recipe("Хлебная кайфуля", [ingredient3, ingredient4])

    shopping_list1 = ShoppingList()
    shopping_list1.add_recipe(recipe1, 1)
    shopping_list2 = ShoppingList()
    shopping_list2.add_recipe(recipe2, 1)

    new_shopping_list = shopping_list1 + shopping_list2

    
    result1 = shopping_list1.get_list()
    result2 = shopping_list2.get_list()
    result_new = new_shopping_list.get_list()

    flour1 = next(ingredient for ingredient in result1 if ingredient.name == "Мука") #next - https://docs.python.org/3/library/functions.html#next
    flour2 = next(ingredient for ingredient in result2 if ingredient.name == "Мука") #next - https://docs.python.org/3/library/functions.html#next
    flour_new = next(ingredient for ingredient in result_new if ingredient.name == "Мука") #next - https://docs.python.org/3/library/functions.html#next

    assert flour1.quantity == 500.0
    assert flour2.quantity == 300.0
    assert flour_new.quantity == 800.0  


     



    