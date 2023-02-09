import datetime
import re

from socialmedia import Socialmedia


class Facebook(Socialmedia):
    DEFAULT_USER_ID = str(datetime.datetime.now().microsecond)

    def __init__(self, nick: str, email: str):
        """
        Создание и инициализация объекта пользователя whatsApp
        :param nick: ник пользователя
        :param email: email пользователя
        """
        self.photo = None
        self.email = None

        self.nick = nick
        self.validate_email(email)

        self.__user_id = Facebook.default_generator()

    def validate_email(self, email):
        if not isinstance(email, str):
            raise TypeError("")
        if re.search(r"[a-zA-Z0-9_]+@[a-zA-Z]+\.[a-zA-Z]+", email):
            self.email = email
        else:
            raise ValueError("")

    def create_clone_page(self):
        super(Facebook, self).create_clone_page()
        return Facebook(nick="Clone_" + self.nick, email=self.email)

    def remove(self):
        super(Facebook, self).remove()
        self.bio = None
        self.photo = None
        self.email = None
        self.nick = "DELETED"

    def __repr__(self):
        return f"{self.__class__.__name__}(nick={self.nick!r}, email={self.email!r}, user_id={self.userid})"

    @property
    def userid(self):
        return self.__user_id

    @userid.setter
    def userid(self, new_id):
        if self.validate_number(new_id):
            self.__user_id = new_id

    @staticmethod
    def validate_number(user_id: int) -> bool:
        """
        Функция валидирует значение номера телефона
        :param user_id: user id
        :return: True, если номер введен корректно
        """
        if not isinstance(user_id, int):
            raise ValueError("")
        return True

    @classmethod
    def default_generator(cls):
        return int(str(datetime.datetime.now().date()).replace("-", "") + \
               str(cls.DEFAULT_USER_ID))
