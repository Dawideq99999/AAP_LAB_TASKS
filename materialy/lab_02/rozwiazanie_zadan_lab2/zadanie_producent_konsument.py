import queue
import threading
import time

# ===== KOLEJKA =====
q = queue.Queue()

# ile liczb generujemy
MAX = 20


# ===== PRODUCENT =====
def producent():
    for i in range(1, MAX + 1):
        print(f"[PRODUCENT] dodaje: {i}")
        q.put(i)
        time.sleep(0.1)

    # sygnał zakończenia
    q.put(None)
    q.put(None)


# ===== KONSUMENT PARZYSTY =====
def konsument_parzyste():
    while True:
        liczba = q.get()

        if liczba is None:
            break

        if liczba % 2 == 0:
            print(f"[PARZYSTE] pobrano: {liczba}")

        q.task_done()


# ===== KONSUMENT NIEPARZYSTY =====
def konsument_nieparzyste():
    while True:
        liczba = q.get()

        if liczba is None:
            break

        if liczba % 2 != 0:
            print(f"[NIEPARZYSTE] pobrano: {liczba}")

        q.task_done()


# ===== WĄTKI =====
t1 = threading.Thread(target=producent)
t2 = threading.Thread(target=konsument_parzyste)
t3 = threading.Thread(target=konsument_nieparzyste)

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

print("\nKONIEC PROGRAMU")