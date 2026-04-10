import requests
import time
import concurrent.futures

CAT_API_URL = "https://catfact.ninja/fact"


# ===== FUNKCJA POBIERAJĄCA FAKT =====
def pobierz_fakt():
    response = requests.get(CAT_API_URL)
    return response.json().get("fact")


# ===== 1. SEKWENCYJNIE =====
def pobierz_sekwencyjnie(liczba):
    start = time.time()

    fakty = []
    for _ in range(liczba):
        fakty.append(pobierz_fakt())

    end = time.time()

    print("\n--- SEKWENCYJNIE ---")
    print(f"Czas: {end - start:.2f} s")
    return fakty


# ===== 2. WIELOWĄTKOWO =====
def pobierz_wielowatkowo(liczba):
    start = time.time()

    with concurrent.futures.ThreadPoolExecutor() as executor:
        fakty = list(executor.map(lambda _: pobierz_fakt(), range(liczba)))

    end = time.time()

    print("\n--- WIELOWĄTKOWO ---")
    print(f"Czas: {end - start:.2f} s")
    return fakty


# ===== URUCHOMIENIE =====
LICZBA = 20

fakty_seq = pobierz_sekwencyjnie(LICZBA)
fakty_thread = pobierz_wielowatkowo(LICZBA)


# ===== PORÓWNANIE =====
print("\n--- PORÓWNANIE ---")
print(f"Pierwszy fakt (seq): {fakty_seq[0]}")
print(f"Pierwszy fakt (thread): {fakty_thread[0]}")