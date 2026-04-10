# ===== DESKRYPTOR =====
class Typed:
    def __init__(self, name, expected_type):
        self.name = name
        self.expected_type = expected_type

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get(self.name)

    def __set__(self, instance, value):
        if not isinstance(value, self.expected_type):
            raise TypeError(
                f"Atrybut '{self.name}' musi być typu {self.expected_type.__name__}"
            )
        instance.__dict__[self.name] = value


# ===== KLASA =====
class Osoba:
    imie = Typed("imie", str)
    wiek = Typed("wiek", int)

    def __init__(self, imie, wiek):
        self.imie = imie
        self.wiek = wiek


# ===== TESTY =====
o = Osoba("Anna", 25)
print(o.imie)
print(o.wiek)

# poprawna zmiana
o.wiek = 30
print(o.wiek)

# błąd
o.wiek = "trzydzieści"