import random
from typing import Optional, Union

from product import Product
from user import User
from password import Password


class Store:
    __psswrd_obj = Password()
    __dir_saved_users = {}

    def __init__(self, user: Optional[str] = None, password: Optional[str] = None):
        self.list_users = []
        user1 = User(user, password)
        Store.__dir_saved_users[user] = Store.__psswrd_obj.get_hash_for_user(password)
        self.list_users.append(user1)

    def remove_product(self, user: Union[str, User], product: Optional[Union[str, Product]] = None):
        if product is None:
            user.basket.remove_product_by_name("all")
        else:
            user.basket.remove_product_by_name(product.name)

    def add_product(self, user: Union[str, User], product: Product):
        if isinstance(user, User):
            if user in self.list_users:
                user.basket.add_product(product)

        elif isinstance(user, str):
            for usr in self.list_users:
                if usr.usrename == user:
                    usr.basket.add_product(product)

        else:
            raise ValueError("Нет такого пользователя!")

    def view_user_cart(self, user: Union[User, str]):
        if isinstance(user, User):
            if user in self.list_users:
                return user.basket.__str__()

        elif isinstance(user, str):
            for usr in self.list_users:
                if usr.usrename == user:
                    return usr.basket.__str__()

    def add_new_user(self, user, password):
        for usr in self.list_users:
            if usr.usrename == user:
                print("Такой пользователь уже есть!")
                raise ValueError("Такой пользователь уже есть!")

        else:
            user1 = User(user, password)
            Store.__dir_saved_users[user] = Store.__psswrd_obj.get_hash_for_user(password)
            self.list_users.append(user1)
            return user1

    def login_user(self, user, password):
        for usr in self.list_users:
            if usr.usrename == user:
                if Store.__psswrd_obj.check_password(password, Store.__dir_saved_users[user]):
                    return usr

        print("Попробуйте еще раз")
        return False

    def get_all_users(self):
        return str(self.list_users)


if __name__ == '__main__':

    list_product = []
    from gen_product import product_gen

    for i in product_gen():
        list_product.append(Product(**i))

    user1 = User("username1", "username1_password")
    user2 = User("username2", "username2_password")
    user3 = User("username3", "username3_password")

    print(user1.__repr__())
    print(user2.__repr__())
    print(user3.__repr__())

    print(user1.basket)

    _input = input("Введие имя пользователя и пароль:\n").split()
    user_name, password = _input[0], _input[1]

    stor1 = Store(*_input)
    stor1.add_product(user_name, random.choice(list_product))
    print("В корзину добавлен рандомный продукт:")
    print(stor1.view_user_cart(user_name))

    _input = input("Добавь нового пользователя (имя и пароль):\n").split()
    user = stor1.add_new_user(*_input)
    print("В магазине зарегистрирован новый пользователь:")
    print(user.__str__())
    print(stor1.get_all_users())

    _input = input("Войдите в систему (имя и пароль), чтобы добавить продукт в корзину пользователя:\n").split()
    user = stor1.login_user(*_input)
    print(user.__str__())

    product_name = random.choice(list_product)
    stor1.add_product(user, product_name)
    print(f"В корзину пользователя {user.__str__()} добавлен продукт {product_name}:")
    print(stor1.view_user_cart(user_name))
    print(f"Из корзины пользователя {user.__str__()} удалить продукт {product_name}:")
    stor1.remove_product(user, product_name)
    print(stor1.view_user_cart(user_name))
