# Создать класс IdCounter (в котором хранятся генератор значений id (обычный инкремент на 1))
# в нем должен быть реализован простой интерфейс хранения значения и получения нового значения
import datetime


class IdCounter:
    __con_current_index = 0

    @staticmethod
    def get_index():
        tmp = IdCounter.__con_current_index
        IdCounter.__con_current_index += 1
        return tmp


if __name__ == '__main__':

    print(IdCounter.get_index())
    print(IdCounter.get_index())
    print(IdCounter.get_index())