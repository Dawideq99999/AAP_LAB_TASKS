import pytest
from product import Product


@pytest.fixture
def product():
    # przykładowa instancja Product do testów
    return Product("Laptop", 100.0, 10)


def test_is_available(product):
    assert product.is_available() is True


@pytest.mark.parametrize("amount, expected_quantity", [
    (5, 15),   # 10 + 5 = 15
    (0, 10),   # 10 + 0 = 10
    (2, 12),   # 10 + 2 = 12
])
def test_add_stock_parametrized(product, amount, expected_quantity):
    product.add_stock(amount)
    assert product.quantity == expected_quantity


def test_remove_stock_too_much_raises(product):
    with pytest.raises(ValueError):
        product.remove_stock(20)


@pytest.mark.parametrize("percent, expected_price", [
    (0, 100.0),    # bez zmian
    (50, 50.0),    # połowa ceny
    (100, 0.0),    # cena = 0
])
def test_apply_discount(product, percent, expected_price):
    product.apply_discount(percent)
    assert product.price == expected_price


@pytest.mark.parametrize("percent", [
    -10,
    -1,
    101,
    150,
])
def test_apply_discount_invalid_values(product, percent):
    with pytest.raises(ValueError):
        product.apply_discount(percent)
#python -m pytest test_product_pytest.py -v