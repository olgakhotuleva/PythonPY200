import unittest
from main import MobileFacebook
from main import Facebook  # импортируем то, что будем тестировать


class MyTestCase1(unittest.TestCase):

    @classmethod
    def setUpClass(cls):  # Определили данные для тестов один раз для всех
        print("setUpClass")
        cls.my_class = MobileFacebook("test", "test@gmail.com")

    @classmethod
    def tearDownClass(cls):  # Очистили после всех тестов
        print("tearDownClass")
        cls.doClassCleanups()

    def test_get_user_id(self):
        print("test_get_user_id")
        self.assertIsNotNone(self.my_class.userid)

    def test_set_os_version(self):
        print("test_set_os_version")
        self.my_class.set_os_version("ios")
        self.assertEqual(self.my_class.mobile_os_version, "ios")

        with self.assertRaises(ValueError):
            self.my_class.set_os_version("new")

    def test_add_friend(self):
        with self.assertRaises(ValueError):
            self.my_class.add_friend(1)

        _list = ["fr1", "fr2"]
        self.my_class.add_friend(_list)
        self.assertCountEqual(_list, self.my_class.list_of_friends)

    def test_create_clone_page(self):
        self.assertIsInstance(self.my_class.create_clone_page(), Facebook)

    def test_remove_page(self):
        _list = ["fr1", "fr2"]
        self.my_class.add_friend(_list)

        self.my_class.remove()
        self.assertEqual(self.my_class.email, None)
        self.assertEqual(self.my_class.nick, "DELETED")
        self.assertCountEqual(self.my_class.list_of_friends, [])

    def test_create_obj_with_invalid_email(self):
        with self.assertRaises(ValueError):
            my_class = MobileFacebook("test", "testXXXgmail.com")

    def test_create_object_from_string(self):
        my_class = MobileFacebook.from_string("test, test@gmail.com")
        self.assertIsInstance(my_class, MobileFacebook)

        self.assertEqual(my_class.nick, "test")
        self.assertEqual(my_class.email, "test@gmail.com")
        self.assertIsNotNone(my_class.userid)


if __name__ == '__main__':
    unittest.main()
