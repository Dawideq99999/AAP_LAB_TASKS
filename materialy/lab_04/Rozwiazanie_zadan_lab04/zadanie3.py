
# Symulacja wyszukiwania wektorowego (semantic search)
# z użyciem cosine similarity

import numpy as np


# =====================================================
# 1. "Baza" filmów z embeddingami
# =====================================================

filmy = {
    "Incepcja": np.array([0.8, 0.3, 0.9]),
    "Matrix": np.array([0.75, 0.35, 0.85]),
    "Toy Story": np.array([0.2, 0.9, 0.1]),
    "Shrek": np.array([0.25, 0.85, 0.15]),
    "Szeregowiec Ryan": np.array([0.6, 0.1, 0.7]),
}


# =====================================================
# 2. Funkcja cosine similarity
# =====================================================

def cosine_similarity(vec1, vec2):
    """
    Oblicza podobieństwo cosinusowe
    między dwoma wektorami
    """

    dot_product = np.dot(vec1, vec2)

    norm_vec1 = np.linalg.norm(vec1)
    norm_vec2 = np.linalg.norm(vec2)

    similarity = dot_product / (norm_vec1 * norm_vec2)

    return similarity


# =====================================================
# 3. Funkcja semantic_search
# =====================================================

def semantic_search(query_vec, database, top_k=3):
    """
    Zwraca top_k najbardziej podobnych filmów
    do podanego wektora query_vec
    """

    results = []

    for title, embedding in database.items():
        sim = cosine_similarity(query_vec, embedding)

        results.append((title, sim))

    # sortowanie malejąco po similarity
    results.sort(key=lambda x: x[1], reverse=True)

    return results[:top_k]


# =====================================================
# 4. Wektor zapytania
# =====================================================

# np. "coś podobnego do sci-fi"
query = np.array([0.7, 0.3, 0.8])


# =====================================================
# 5. Uruchomienie wyszukiwania
# =====================================================

results = semantic_search(query, filmy, top_k=3)


# =====================================================
# 6. Wyniki
# =====================================================

print("===================================")
print("TOP 3 najbardziej podobne filmy")
print("===================================")

for title, sim in results:
    print(f"{title}: {sim:.3f}")