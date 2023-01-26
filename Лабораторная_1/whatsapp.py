class WhatsApp:
    def __init__(self, name, number):
        """
        Создание и инициализация объекта пользователя whatsApp
        :param name: имя пользователя
        :param number: номер телефон
        Примеры:
        >>> user_1 = WhatsApp("Олег Олегович", 12345)  # инициализация экземпляра класса
        """
        self.name = name
        self.photo = None
        self.number = None

        if self.validate_number(number):
            self.number = number

    def set_photo(self, photo) -> None:
        """
        Функция позволяет пользователю добать вотографию
        :param photo:
        :return:
        """
        self.photo = photo

    def change_number(self, new_number: int) -> None:
        """
        Функция меняет значение номера телефона уже существующего пользователя
        :param new_number:

        >>> user_1 = WhatsApp("First_name Second_name", 12345)  # инициализация экземпляра класса
        >>> user_1.change_number("ddddd")
        Traceback (most recent call last):
        ValueError: Telephone number value must contain only numbers
        """
        if self.validate_number(new_number):
            self.number = new_number

    def validate_number(self, _number: int) -> bool:
        """
        Функция валидирует значение номера телефона
        :param _number: номер телефона
        :return: True, если номер введен корректно
        >>> user_1 = WhatsApp("First_name Second_name", 12345)  # инициализация экземпляра класса
        """
        if not isinstance(_number, int):
            raise ValueError("Telephone number value must contain only numbers")
        return True


if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    import doctest
    doctest.testmod()
