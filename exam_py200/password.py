# Создать класс Password (который ответственен за выдачу хэш-значения пароля и проверке пароля с его хэш значением)
# реализовать методы get и check
# get - выдаёт хэш-значение. Можно возпользоваться модулем hashlib. Как пример и для упрощения предлагаю воспользоваться данным выражением hashlib.sha256(password.encode()).hexdigest(), которое вернёт хэш-значение по переданной строке password. Однако вы сами вольны выбирать каким методом и как возвращать хэш-значение.
# Для передаваемого пароля перед получением хэш-значения должны быть произведены проверки, что пароль строкового типа и пароль соответствует минимальным правилам (проверить можно как при помощи re, так и обычных строковых методов) пароля:
# Длина не менее 8 символов
# В пароле есть как цифры так и буквы
# check - проверяет соотносится ли передаваемый пароль с его хэш-значением

import hashlib

class Password:

    def __init__(self):
        self.psswd_checker = {}

    def get_hash(self, _password):

        self.validate_password(_password)

        self.psswd_checker[_password] = hashlib.sha256(_password.encode()).hexdigest()

        return self.psswd_checker[_password]

    def _check_password(self, _password, _hash):
        if self.psswd_checker.get(_password):
            return True
        else:
            return False

    def validate_password(self, _password):
        if len(_password) < 8:
            raise ValueError("")
        # TODO
