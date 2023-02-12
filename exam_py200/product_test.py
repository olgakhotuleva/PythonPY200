import unittest
from product import Product


class ProductTestCase1(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("setUpClass")
        cls.my_class = Product("стол_кухонный", 100, 4.6)

    @classmethod
    def tearDownClass(cls):
        print("tearDownClass")
        cls.doClassCleanups()

    def test_get_name(self):
        print("test_get_name")
        self.assertEqual(self.my_class.name, "стол_кухонный")

    def test_get_rating(self):
        print("test_get_rating")
        self.assertEqual(self.my_class.rating, 4.6)

    def test_set_rating(self):
        print("test_set_rating")
        self.my_class.rating = 5
        self.assertEqual(self.my_class.rating, 5)

    def test_set_rating_negative(self):
        print("test_set_rating")
        with self.assertRaises(ValueError):
            self.my_class.rating = -7

    def test_set_rating_negative2(self):
        print("test_set_rating")
        with self.assertRaises(TypeError):
            self.my_class.rating = "1"

    def test_set_price(self):
        print("test_set_price")
        self.my_class.price = 5
        self.assertEqual(self.my_class.price, 5)

    def test_set_price_negative(self):
        print("test_set_price")
        with self.assertRaises(ValueError):
            self.my_class.price = -7


if __name__ == '__main__':
    unittest.main()
