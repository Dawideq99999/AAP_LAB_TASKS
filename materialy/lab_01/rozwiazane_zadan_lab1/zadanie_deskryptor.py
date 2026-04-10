from datetime import datetime


# ===== DESKRYPTOR =====
class LogowanyAtrybut:
    def __init__(self, nazwa):
        self.nazwa = nazwa

    def __get__(self, instance, owner):
        if instance is None:
            return self
        
        wartosc = instance.__dict__.get(self.nazwa)
        print(f"[{datetime.now()}] ODCZYT {self.nazwa} = {wartosc}")
        return wartosc

    def __set__(self, instance, value):
        print(f"[{datetime.now()}] ZAPIS {self.nazwa} = {value}")
        instance.__dict__[self.nazwa] = value


# ===== KLASA =====
class Uzytkownik:
    imie = LogowanyAtrybut("imie")
    wiek = LogowanyAtrybut("wiek")

    def __init__(self, imie, wiek):
        self.imie = imie
        self.wiek = wiek


# ===== TEST =====
u = Uzytkownik("Anna", 25)

print(u.imie)   # odczyt
u.wiek = 30     # zapis
print(u.wiek)   # odczyt