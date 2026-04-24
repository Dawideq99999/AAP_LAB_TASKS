
import unittest
from product import Product


class TestProduct(unittest.TestCase):

    def setUp(self):
        # tworzenie przykładowego produktu przed każdym testem
        self.product = Product("Laptop", 2999.99, 10)

    def test_add_stock_positive(self):
        self.product.add_stock(5)
        self.assertEqual(self.product.quantity, 15)

    def test_add_stock_negative_raises(self):
        with self.assertRaises(ValueError):
            self.product.add_stock(-3)

    def test_remove_stock_positive(self):
        self.product.remove_stock(4)
        self.assertEqual(self.product.quantity, 6)

    def test_remove_stock_too_much_raises(self):
        with self.assertRaises(ValueError):
            self.product.remove_stock(20)

    def test_is_available_when_in_stock(self):
        self.assertTrue(self.product.is_available())

    def test_is_not_available_when_empty(self):
        empty_product = Product("Mouse", 99.99, 0)
        self.assertFalse(empty_product.is_available())

    def test_total_value(self):
        self.assertEqual(self.product.total_value(), 2999.99 * 10)


if __name__ == "__main__":
    unittest.main()


    # do uruchomienia testow python -m unittest test_product_unittest -v