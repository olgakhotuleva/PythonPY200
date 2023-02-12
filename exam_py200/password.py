# Создать класс Password (который ответственен за выдачу хэш-значения пароля и проверке пароля с его хэш значением)
# реализовать методы get и check
# get - выдаёт хэш-значение. Можно возпользоваться модулем hashlib. Как пример и для упрощения предлагаю воспользоваться данным выражением hashlib.sha256(password.encode()).hexdigest(), которое вернёт хэш-значение по переданной строке password. Однако вы сами вольны выбирать каким методом и как возвращать хэш-значение.
# Для передаваемого пароля перед получением хэш-значения должны быть произведены проверки, что пароль строкового типа и пароль соответствует минимальным правилам (проверить можно как при помощи re, так и обычных строковых методов) пароля:
# Длина не менее 8 символов
# В пароле есть как цифры так и буквы
# check - проверяет соотносится ли передаваемый пароль с его хэш-значением

import hashlib


class Password:

    #def __init__(self):
        #self.psswd_checker = {}

    @staticmethod
    def get_hash_for_user( _password):
        Password.__validate_password(_password)

        return hashlib.sha256(_password.encode()).hexdigest()

    @staticmethod
    def check_password(_password, _hash):
        if hashlib.sha256(_password.encode()).hexdigest() == _hash:
            return True
        else:
            return False
    @staticmethod
    def __validate_password(_password):
        if not isinstance(_password, str):
            raise ValueError("")
        if len(_password) < 8:
            raise ValueError("")
        # TODO
