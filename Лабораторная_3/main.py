from typing import Union


class Book:
    """ Базовый класс книги. """

    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"

    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super(PaperBook, self).__init__(name, author)
        self._pages = pages

    # def __str__(self):
    #     return super().__str__()

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages!r})"

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, pages_: int):
        if not isinstance(pages_, int):
            raise TypeError("Количество страниц может быть только целым положительным числом")
        if pages_ < 0:
            raise ValueError("Количество страниц может быть только целым положительным числом")

        self._pages = pages_


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super(AudioBook, self).__init__(name, author)
        self._duration = duration

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.duration!r})"

    # def __str__(self):
    #     return super().__str__()
    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, duration_: Union[float, int]):

        if not isinstance(duration_, (int, float)):
            raise TypeError("Длительность книги может быть только положительным числом")
        if duration_ < 0:
            raise ValueError("Длительность книги может быть только положительным числом")

        self._duration = duration_


if __name__ == "__main__":
    c1 = AudioBook("name1", "aothor1", duration=2.5)
    c2 = PaperBook("name2", "aothor2", pages=100)

    # c1.name = "new_name1"
    print(c1.name)
    c2.pages = -20
    #c1.duration = -3.6
    print(c1.duration)

    print(c1)
    print(c2)

    print(c1.__repr__())
    print(c2.__repr__())
