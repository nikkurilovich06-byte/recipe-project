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

if __name__ == "__main__":
    print("Проверка класса Ingredient")

    ingr1 = Ingredient("Мука", 500, "г")
    print(ingr1)
    print(repr(ingr1))

    try:
        ingr1.quantity = -300
        print(ingr1.quantity)
    except ValueError as error:
        print("Ожидаемая ошибка:", error)