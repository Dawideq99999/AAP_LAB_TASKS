
from pymongo import MongoClient
import requests

# =====================================================
# 1. Połączenie z MongoDB
# =====================================================

# połączenie z lokalnym serwerem MongoDB
client = MongoClient("mongodb://localhost:27017")

# tworzenie / wybór bazy danych
db = client["lab4"]

# tworzenie / wybór kolekcji
networks = db["networks"]


# =====================================================
# 2. Wyczyść starą kolekcję (opcjonalnie)
# =====================================================

# żeby nie duplikować danych przy kolejnym uruchomieniu
networks.delete_many({})


# =====================================================
# 3. Pobranie danych z API GeckoTerminal
# =====================================================

response = requests.get(
    "https://api.geckoterminal.com/api/v2/networks"
)

# pobranie listy dokumentów
data = response.json()["data"]


# =====================================================
# 4. Wstawienie dokumentów do MongoDB
# =====================================================

# MongoDB przyjmuje listę dict bezpośrednio
networks.insert_many(data)

print("Dane zostały zapisane do MongoDB.\n")


# =====================================================
# 5. Agregacja:
# ile sieci przypada na każdy typ?
# =====================================================

print("===================================")
print("Liczba sieci dla każdego typu")
print("===================================")

pipeline = [
    {
        "$group": {
            "_id": "$attributes.type",
            "count": {
                "$sum": 1
            }
        }
    },
    {
        "$sort": {
            "count": -1
        }
    }
]

for doc in networks.aggregate(pipeline):
    print(doc)


# =====================================================
# 6. Zamknięcie połączenia
# =====================================================

client.close()