from idcouter import IdCounter
from cart import Cart
from password import Password


class User:
    default_password = 'password1'
    _password = Password()

    def __init__(self, _user, _password):
        self.__id = IdCounter.get_index()

        # add user verification
        self.__username = _user
        self.__password = User._password.get_hash(_password)  # hash

        self.__basket = Cart()

    @property
    def basket(self):
        return self.__basket.__str__()

    def __repr__(self):
        return f"{self.__class__.__name__}(id={self.__id}, username={self.__username}, " \
               f"password={self.default_password})"

    def __str__(self):
        return f"({self.__id}, {self.__username})"
