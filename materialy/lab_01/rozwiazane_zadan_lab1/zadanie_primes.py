# ===== SPRAWDZANIE CZY LICZBA JEST PIERWSZA =====
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


# ===== GENERATOR LICZB PIERWSZYCH =====
def prime_generator():
    n = 2
    while True:
        if is_prime(n):
            yield n
        n += 1


# ===== GENERATOR TYLKO LICZB KOŃCZĄCYCH SIĘ NA 7 =====
primes_ending_with_7 = (p for p in prime_generator() if p % 10 == 7)


# ===== TEST =====
for _ in range(10):
    print(next(primes_ending_with_7))