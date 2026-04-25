# Zadanie 1 · SQLite + Random User API
# Cel:
# 1. Pobierz 30 użytkowników z API
# 2. Zapisz ich do tabeli SQL
# 3. Wykonaj zapytania analityczne

import sqlite3
import requests

# =====================================================
# 1. Połączenie z bazą SQLite
# =====================================================

# tworzy plik users.db jeśli jeszcze nie istnieje
conn = sqlite3.connect("users.db")

# cursor pozwala wykonywać komendy SQL
cursor = conn.cursor()


# =====================================================
# 2. Utworzenie tabeli Users
# =====================================================

# usuwamy starą tabelę (żeby nie duplikować danych przy kolejnym uruchomieniu)
cursor.execute("DROP TABLE IF EXISTS Users")

# tworzymy nową tabelę
cursor.execute("""
CREATE TABLE Users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT,
    last_name TEXT,
    email TEXT,
    address TEXT,
    age INTEGER,
    gender TEXT,
    country TEXT
)
""")


# =====================================================
# 3. Pobranie danych z Random User API
# =====================================================

response = requests.get("https://randomuser.me/api/?results=30")

# zamiana odpowiedzi JSON na słownik Pythona
data = response.json()

# lista 30 użytkowników
users = data["results"]


# =====================================================
# 4. Wstawianie danych do tabeli
# =====================================================

for user in users:
    first_name = user["name"]["first"]
    last_name = user["name"]["last"]
    email = user["email"]

    # pełny adres jako jeden tekst
    street_number = str(user["location"]["street"]["number"])
    street_name = user["location"]["street"]["name"]
    city = user["location"]["city"]
    country = user["location"]["country"]

    address = f"{street_number} {street_name}, {city}"

    age = user["dob"]["age"]
    gender = user["gender"]

    # INSERT z parametryzacją (?, ?, ?)
    # NIE używamy f-stringów w SQL
    cursor.execute("""
        INSERT INTO Users (
            first_name,
            last_name,
            email,
            address,
            age,
            gender,
            country
        )
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        first_name,
        last_name,
        email,
        address,
        age,
        gender,
        country
    ))


# zapis zmian do bazy
conn.commit()


# =====================================================
# 5. Zapytania analityczne
# =====================================================

print("===================================")
print("1. Ilu jest mężczyzn, a ile kobiet?")
print("===================================")

cursor.execute("""
    SELECT gender, COUNT(*)
    FROM Users
    GROUP BY gender
""")

for row in cursor.fetchall():
    print(f"{row[0]}: {row[1]}")


print("\n======================")
print("2. Jaki jest średni wiek?")
print("======================")

cursor.execute("""
    SELECT AVG(age)
    FROM Users
""")

avg_age = cursor.fetchone()[0]
print(f"Średni wiek: {avg_age:.2f}")


print("\n===================================")
print("3. W ilu krajach mieszkają użytkownicy?")
print("===================================")

cursor.execute("""
    SELECT COUNT(DISTINCT country)
    FROM Users
""")

countries_count = cursor.fetchone()[0]
print(f"Liczba krajów: {countries_count}")


print("\n===================================")
print("Dodatkowo: użytkownicy wg krajów")
print("===================================")

cursor.execute("""
    SELECT country, COUNT(*)
    FROM Users
    GROUP BY country
    ORDER BY COUNT(*) DESC
""")

for row in cursor.fetchall():
    print(f"{row[0]}: {row[1]}")


# =====================================================
# 6. Zamknięcie połączenia
# =====================================================

conn.close()