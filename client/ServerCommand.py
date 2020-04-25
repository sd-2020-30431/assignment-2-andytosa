from User import User
from FoodItem import FoodItem

class ServerCommand:
    def registerUser(self, user):
        return f"INSERT INTO users (username, password, email) VALUES ('{user.username}', '{user.password}', '{user.email}');"


    def addFood(self, food):
        return f"""INSERT INTO foods (name, quantity, calories, buy_date, exp_date, user_id) VALUES (
            {food.name},
            {food.quantity},
            {food.calories}, 
            {food.buy_date}, 
            {food.exp_date}, 
            {food.user_id}
            );"""
    
    
    def selectFood(self, user_id):
        return f"SELECT * FROM foods WHERE foods.user_id = {user_id}"


    def getCommand(self, action):
        if action == 'register':
            username = input('username: ')
            password = input('password: ')
            email = input('email: ')

            return self.registerUser(User(username, password, email))
        
        if action == 'select':
            user_id = input('user_id')

            return self.selectFood(user_id)


