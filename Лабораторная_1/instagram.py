class Instagram:
    def __init__(self, nick: str, email: str):
        """
        Создание и инициализация объекта пользователя whatsApp
        :param nick: ник пользователя
        :param email: email пользователя
        Примеры:
        >>> user_1 = Instagram("User_1", "w@ya.ru")  # инициализация экземпляра класса
        """
        self.bio = None
        self.photo = None
        self.nick = nick
        self.email = email

    def add_bio(self, bio: str) -> None:
        """
        Функция добавляет bio в описание профиля пользователя
        Проверяет ограничение на 500 символов
        :param bio:

        >>> user_1 = Instagram("User_1", "w@ya.ru")
        >>> user_1.add_bio("It is my new account")
        """
        if len(bio) > 500:
            raise ValueError("There is a limit on the number of characters:"
                             " no more than 500")
        self.bio = bio

    def change_nick(self, new_nick: str) -> str:
        """
           Функция позволяет изменить свой niсk пользователю
           :param new_nick: новый ник пользователя
           :return:

            >>> user_1 = Instagram("User_1", "w@ya.ru")
            >>> user_1.change_nick("New_user_2")
            'New_user_2'
        """
        self.nick = new_nick
        return self.nick

    def __str__(self):
        return f"Instagram({self.nick}, {self.email})"


if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    import doctest
    doctest.testmod()
