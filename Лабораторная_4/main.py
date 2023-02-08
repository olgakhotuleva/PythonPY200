from typing import Union, Optional
import datetime

from facebook import Facebook
from instagram import Instagram


class MobileFacebook(Facebook):
    #DEFAULT_USER_ID = 0

    def __init__(self, nick: str, email: str):
        super(MobileFacebook, self).__init__(nick, email)
        self.mobile_os_version = None
        self.list_of_friends = []

    def set_os_version(self, os):
        if os in ["ios", "Android"]:
            self.mobile_os_version = os
        else:
            raise ValueError("Unknown os version")

    def add_friend(self, name: Union[list, str]):
        if isinstance(name, list):
            self.list_of_friends.extend(name)

        elif isinstance(name, str):
            self.list_of_friends.append(name)
        else:
            raise ValueError("Empty Value")

    def remove(self):
        print(f"Расширенный метод remove для {self.__class__.__name__}")
        super().remove()
        self.list_of_friends.clear()

    def __str__(self):
        return f"{self.__class__.__name__}(nick={self.nick!r}, email={self.email!r}," \
               f" friends={len(self.list_of_friends)}, user_id={self.userid}) "

    @classmethod
    def from_string(cls, data_string):
        "Мeтод позволяет создать пользователя из строки)"
        data_string=data_string.replace(" ", "")
        nick, email = data_string.split(",")
        return cls(nick, email)


class DesktopFacebook(Facebook):
    def __init__(self, nick: str, email: str):
        super(DesktopFacebook, self).__init__(nick, email)
        self.os_version = None


if __name__ == "__main__":
    fb1 = Facebook(nick="account1", email="xxx@gmail.com")
    print(f"Юзер Facebook => {fb1}\n")

    fb_mobile1 = MobileFacebook("acc+mob1", "accmob1@gamil.com")
    print(f"Юзер MobileFacebook => {fb_mobile1}")
    # fb_mobile1.add_friend(["new friend", "new_friend_2"])
    fb_mobile1.add_friend("new friend")
    print(f"Юзер MobileFacebook, add friend => {fb_mobile1}\n")

    new_fb_mb = fb_mobile1.create_clone_page()
    print(f"{new_fb_mb}\n")

    test_user = MobileFacebook.from_string("test_account, test_account@gmail.com")
    print(f"Юзер созданный из строки {new_fb_mb}\n")

    fb_mobile1.remove()
    print(fb_mobile1)

    fb_desktop1 = DesktopFacebook("acc+mob1", "accmob1@gmail.com")
    print(fb_desktop1)
    fb_desktop1.remove()
    print(fb_desktop1)

    inst1 = Instagram("inst1", "inst1@gmail.com")
    print(inst1)
