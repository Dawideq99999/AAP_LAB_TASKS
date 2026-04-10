from functools import wraps
from datetime import datetime
import time

# ===== DEKORATOR 1 =====
def liczba_elementow_list(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        for arg in args:
            if isinstance(arg, list):
                print(f"Lista ma {len(arg)} elementów")

        for value in kwargs.values():
            if isinstance(value, list):
                print(f"Lista ma {len(value)} elementów")

        return func(*args, **kwargs)
    return wrapper


# ===== DEKORATOR 2 =====
def logger(nazwa_pliku):
    def dekorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start = time.time()

            wynik = func(*args, **kwargs)

            end = time.time()
            czas = end - start

            data = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            with open(nazwa_pliku, "a") as f:
                f.write(f"{data} | {func.__name__} | {czas:.6f} s\n")

            return wynik
        return wrapper
    return dekorator


# ===== TESTY =====
@liczba_elementow_list
def funkcja1(a, b):
    print("Funkcja 1 działa")

@logger("log.txt")
def funkcja2():
    time.sleep(1)
    print("Funkcja 2 działa")


# ===== URUCHOMIENIE =====
funkcja1([1, 2, 3], 5)
funkcja2()