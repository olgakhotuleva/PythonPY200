# TODO Написать 3 класса с документацией и аннотацией типов
from instagram import Instagram

if __name__ == "__main__":

    us1 = Instagram("User_1", "w@ya.ru")
    print(us1)
    us1.change_nick("New_user_2")
    print(us1)
