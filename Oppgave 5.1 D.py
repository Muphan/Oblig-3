"""
AI: Google Gemini
Prompt:
Opprett en liste med filmer (hvor hver film er en egen dictionary med dataene om én film).
Dataene om en film skal minst være: name, year og rating.
Legg til filmene:
Inception – 2010 – 8.7
Inside Out – 2015 – 8.1
Con Air – 1997– 6.9

Opprett en funksjon som legger til en film i filmlisten. Denne funksjonen skal være definert slik at den minst tar følgende parametere:
Listen filmen skal legges til i
name
year
rating

Benytt funksjonen til å legge til 3 filmer du selv bestemmer.

Hvis det ikke er noen rating, skal default rating settes til 5.0
"""


# 1. Oppretter listen med de opprinnelige filmene
movies = [
    {"name": "Inception", "year": 2010, "rating": 8.7},
    {"name": "Inside Out", "year": 2015, "rating": 8.1},
    {"name": "Con Air", "year": 1997, "rating": 6.9}
]

# 2. Oppretter funksjonen med default-verdi for rating
def add_movie(movie_list, name, year, rating=5.0):
    """Legger til en ny film som en dictionary i den valgte filmlisten."""
    new_movie = {
        "name": name,
        "year": year,
        "rating": rating
    }
    movie_list.append(new_movie)

# 3. Legger til 3 nye filmer med funksjonen
add_movie(movies, "The Matrix", 1999, 8.7)
add_movie(movies, "Interstellar", 2014, 8.6)
add_movie(movies, "En helt ukjent film", 2024)  # Benytter default rating (5.0)

# Skriver ut resultatene for å verifisere
for movie in movies:
    print(f"{movie['name']} ({movie['year']}) - Rating: {movie['rating']}")

"""
=============================================
Kjøreeksempel:
=============================================
Inception (2010) - Rating: 8.7
Inside Out (2015) - Rating: 8.1
Con Air (1997) - Rating: 6.9
The Matrix (1999) - Rating: 8.7
Interstellar (2014) - Rating: 8.6
En helt ukjent film (2024) - Rating: 5.0

Process finished with exit code 0

"""