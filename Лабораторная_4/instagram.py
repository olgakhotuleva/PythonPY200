from socialmedia import Socialmedia


class Instagram(Socialmedia):
    def __init__(self, nick: str, email: str):
        """
        Создание и инициализация объекта пользователя
        :param nick: ник пользователя
        :param email: email пользователя
        Примеры:
        """
        self.bio = None
        self.photo = None
        self.nick = nick
        self.email = email

    def create_clone_page(self):
        super(Instagram, self).create_clone_page()
        return Instagram(nick="Clone" + self.nick, email=self.email)

    def remove(self):
        super(Instagram, self).remove()
        self.bio = None
        self.photo = None
        self.email = None
        self.nick = "DELETED"

    def add_bio(self, bio: str) -> None:
        """
        Функция добавляет bio в описание профиля пользователя
        Проверяет ограничение на 500 символов
        :param bio:
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
        """
        self.nick = new_nick
        return self.nick

    def __str__(self):
        return f"Instagram({self.nick}, {self.email})"

    def __repr__(self):
        return f"{self.__class__.__name__}(nick={self.nick!r}, email={self.email!r}, bio={self.bio}"
