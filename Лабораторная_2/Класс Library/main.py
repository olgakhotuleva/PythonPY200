from typing import Iterable

BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


# TODO написать класс Book
class Book:
    def __init__(self, id_: int, name: str, pages: int):
        """
        Создание и инициализация объекта книга
        :param id_: id книги
        :param name: имя книги
        :param pages: количество страниц
        """
        self.id_ = id_
        self.name = name
        self.pages = pages

    def __str__(self):
        return f"Книга \"{self.name}\""

    def __repr__(self):
        return f"{self.__class__.__name__}(id_={self.id_}, name='{self.name}', pages={self.pages})"


# TODO написать класс Library

class Library:
    def __init__(self, books: Iterable = None):
        """
        Создание и инициализация объекта библиотека
        :param books: список книг
        :param index: индекс последней книги
        """
        if books is None:
            self.books = []
        else:
            self.books = books

        self.len = len(self.books)

    def get_next_book_id(self):
        """
        Метод, возвращающий идентификатор/порядковый номер для добавления новой книги в библиотеку.
        :return ind(len+1):идентификатор последней книги увеличенный на 1
        """
        if self.len == 0:
            return 1
        else:
            return self.len + 1  # что такое идентификатор - порядковый номер? 1, 2,3 ..

    def get_index_by_book_id(self, index: int) -> int:
        """
        Метод,  возвращающий индекс книги в списке, который хранится в атрибуте экземпляра класса.
        :param index книги
        :return index: индекс книги из списка
        :raise: ValueError: Если книги нет
        """
        for ind, book in enumerate(self.books):
            if book.id_ == index:
                return ind
        else:
            raise ValueError("Книги с запрашиваемым id не существует")


if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    #print([book.__str__() for book in list_books])

    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
