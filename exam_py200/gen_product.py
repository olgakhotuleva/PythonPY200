from collections.abc import Iterable
import random

PRODUCTS = ["кресло", "стол_кухонный", "стол писменный", "журнальный стол", "офисное кресло"]


def gen_field_rating() -> Iterable[int]:
    """Функция генерирует случайным образом рейтинг. Диапазон 0-5"""
    yield round(random.uniform(0, 5), 2)


def gen_field_price() -> Iterable[int]:
    """Функция генерирует случайным образом цену"""
    yield round(random.uniform(100, 2000), 2)


def product_gen() -> Iterable[dict]:
    """функция генератор
        :return: возвращает итератор словаря
    """
    for _ in PRODUCTS:
        yield dict({
            "name": _,
            "price": next(gen_field_price()),
            "rating": next(gen_field_rating())})
