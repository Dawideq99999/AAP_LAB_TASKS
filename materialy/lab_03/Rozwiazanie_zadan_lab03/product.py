class Product:
    """Reprezentuje produkt w sklepie internetowym."""

    def __init__(self, name: str, price: float, quantity: int):
        # walidacja danych
        if price < 0:
            raise ValueError("Cena nie może być ujemna")
        if quantity < 0:
            raise ValueError("Ilość nie może być ujemna")

        self.name = name
        self.price = price
        self.quantity = quantity

    def add_stock(self, amount: int):
        # dodanie do magazynu
        if amount < 0:
            raise ValueError("Nie można dodać ujemnej ilości")

        self.quantity += amount

    def remove_stock(self, amount: int):
        # usunięcie z magazynu
        if amount < 0:
            raise ValueError("Nie można usunąć ujemnej ilości")

        if amount > self.quantity:
            raise ValueError("Za mało produktów w magazynie")

        self.quantity -= amount

    def is_available(self) -> bool:
        # dostępność produktu
        return self.quantity > 0

    def total_value(self) -> float:
        # całkowita wartość magazynowa
        return self.price * self.quantity

    def apply_discount(self, percent: float):
        """Obniża cenę o podany procent (0–100)."""
        if percent < 0 or percent > 100:
            raise ValueError("Procent rabatu musi być w zakresie 0-100")

        self.price = self.price * (1 - percent / 100)
        ###############################################