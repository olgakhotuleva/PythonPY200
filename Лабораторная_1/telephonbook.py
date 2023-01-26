from typing import Optional, Union


class TelephonBook:
    def __init__(self, name: str, number: int,
                 organization: Optional[Union[str, int]] = None,
                 position: Optional[Union[str, int]] = None):
        """
        Создание нового контакта в телефонной книжке
        :param name: имя пользователя
        :param number: номер телефон
        Примеры:
        >>> user_1 = TelephonBook("Олег Олегович", 89991113444)  # инициализация экземпляра класса
        """
        self.name = name
        if len(str(number)) > 11:
            ValueError("Не валидное значение номера телефона")
            self.number = number

        self.organization = organization
        self.position = position

        self.addithion_info = None

    def add_organization(self, info: str) -> None:
        """Функция добавляет информацию о контакте"""
        self.organization = info

    def remove_addithion_infor(self) -> None:
        """Функция удаляет всю дополнительную информацию о контакте"""
        if self.position:
            self.position = None
        if self.organization:
            self.organization = None
        if self.addithion_info:
            self.addithion_info = None


if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    import doctest

    doctest.testmod()
