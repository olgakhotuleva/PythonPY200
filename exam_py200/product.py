from idcouter import IdCounter


class Product(object):

    def __init__(self, name, price, rating):

        self.__id = IdCounter.get_index()
        self.__name = name

        if self.__validate_value(price):
            self.__price = price
        if self.__validate_value(rating):
            self.__rating = rating

    @property
    def name(self):
        return self.__name

    @property
    def rating(self):
        return self.__rating

    @rating.setter
    def rating(self, _rt):
        if self.__validate_value(_rt):
            self.__rating = _rt

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, _pr):
        if self.__validate_value(_pr):
            self.__price = _pr

    @staticmethod
    def __validate_value(_pr):
        if not isinstance(_pr, (float, int)):
            raise TypeError
        if _pr < 0:
            raise ValueError

    def __repr__(self):
        return f"{self.__class__.__name__}(id={self.__id}, name='{self.__name}', " \
               f"rating={self.__rating}), price={self.__price})"

    def __str__(self):
        return f"({self.__id}, {self.__name})"
