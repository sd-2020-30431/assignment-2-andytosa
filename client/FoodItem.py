import datetime

class FoodItem:
    def __init__(self, name, quantity, calories, buy_date, exp_date):
        self.name = name
        self.quantity = quantity
        self.calories = calories
        self.buy_date = buy_date
        self.exp_date = exp_date

    def __str__(self):
        return f"{self.name} x{self.quantity}: {self.calories}cal"
