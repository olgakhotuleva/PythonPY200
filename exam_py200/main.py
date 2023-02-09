from product import Product
from user import User


# класс Store.
# Реализуйте в нём аутентификацию (упростим задачу, чтобы не хранить список пользователей, под аутентификацией будем понимать создание пользователя) пользователя через консоль(логин и пароль будут вводиться через консоль)
# Реализуйте метод позволяющий пользователю добавить случайный продукт в корзину
# Реализуйте метод позволяющий пользователю просмотреть свою корзину

class Store:

    def __init__(self):
        pass




if __name__ == '__main__':

    user1 = User("username1", "username1_password")
    user2 = User("username2", "username2_password")
    user3 = User("username3", "username3_password")

    print(user1)
    print(user2)
    print(user3)

    print(user1.__repr__())
    print(user2.__repr__())
    print(user3.__repr__())

    print(user1.basket)



