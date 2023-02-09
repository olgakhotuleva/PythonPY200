from product import Product
from typing import Optional, Union


class Cart:
    def __init__(self, _prod: Optional[Product] = None):

        self.products = []
        if self._validate_product(_prod):
            self.products.append(_prod)

    def add_product(self, _prod):
        if self._validate_product(_prod):
            self.add_product(_prod)
        else:
            # raise ValueError("Добавте продукт!")
            print("Добавте продукт!")

    def remove_product_by_name(self, _name):
        for product in self.products:
            if product.name == _name:
                self.products.remove(product)
                break
        else:
            # raise ValueError("Продукт не найден в корзине")
            print("Продукт не найден в корзине")

    @staticmethod
    def _validate_product(_prod):
        if not isinstance(_prod, (Product, type(None))):
            raise TypeError("")
        if isinstance(_prod, type(None)):
            return False
        else:
            return True

    def __str__(self):
        return f"Количество продуктов в корзне = {len(self.products)}"
