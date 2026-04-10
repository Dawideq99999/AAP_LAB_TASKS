import multiprocessing
import time
from lab2_functions import calculate_power_sum


# ===== SEKWENCYJNIE =====
def run_sequential(data):
    start = time.time()

    results = [calculate_power_sum(n) for n in data]

    end = time.time()
    print(f"\nSEKWENCYJNIE: {end - start:.2f} s")
    return results


# ===== WIELOPROCESOWO =====
def run_parallel(data):
    start = time.time()

    with multiprocessing.Pool() as pool:
        results = pool.map(calculate_power_sum, data)

    end = time.time()
    print(f"WIELOPROCESOWO: {end - start:.2f} s")
    return results


# ===== URUCHOMIENIE =====
if __name__ == "__main__":
    data = list(range(1, 500))  # możesz zwiększyć np. do 1000 lub 10000

    wynik1 = run_sequential(data)
    wynik2 = run_parallel(data)

    print("\nPORÓWNANIE:")
    print(f"Pierwszy wynik: {wynik1[0]}")