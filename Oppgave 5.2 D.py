"""
Prompt:
Utvid forrige oppgave med noen funksjoner og benytt dem i koden din.

A) Lag en funksjon som printer ut alle filmene i en gitt liste med filmer
slik at formatet for hver filmutskrift blir seende slik ut:
The Lion King - 1994 has a rating of 8.5

B) Lag en funksjon som tar en liste med filmer som parameter og regner ut gjennomsnittsratingen
 for alle filmene i lista og returnerer dette. Test funksjonen og skriv ut gjennomsnittet.

C) Lag en funksjon som tar en liste med filmer og et årstall som parametere,
og returnerer en ny liste med alle filmer fra og med det gitte årstallet.
Benytt funksjonen, og print ut informasjon om alle filmer fra og med 2010
"""


# 1. Oppretter filmlisten fra forrige oppgave
movies = [
    {"name": "Inception", "year": 2010, "rating": 8.7},
    {"name": "Inside Out", "year": 2015, "rating": 8.1},
    {"name": "Con Air", "year": 1997, "rating": 6.9},
    {"name": "The Lion King", "year": 1994, "rating": 8.5},
    {"name": "Interstellar", "year": 2014, "rating": 8.6},
]


# A) Funksjon som printer alle filmer i et bestemt format
def print_movies(movie_list):
    for movie in movie_list:
        print(f"{movie['name']} - {movie['year']} has a rating of {movie['rating']}")


# B) Funksjon som beregner og returnerer gjennomsnittsratingen
def get_average_rating(movie_list):
    if not movie_list:
        return 0.0
    total_rating = sum(movie["rating"] for movie in movie_list)
    return total_rating / len(movie_list)


# C) Funksjon som returnerer filmer fra og med et gitt årstall
def get_movies_from_year(movie_list, year):
    return [movie for movie in movie_list if movie["year"] >= year]


# --- TESTING AV FUNKSJONENE ---

print("--- A: Alle filmer ---")
print_movies(movies)

print("\n--- B: Gjennomsnittsrating ---")
avg = get_average_rating(movies)
print(f"Gjennomsnittsrating for alle filmene: {avg:.2f}")

print("\n--- C: Filmer fra og med 2010 ---")
recent_movies = get_movies_from_year(movies, 2010)
print_movies(recent_movies)

"""
=============================================
Kjøreeksempel:
=============================================
--- A: Alle filmer ---
Inception - 2010 has a rating of 8.7
Inside Out - 2015 has a rating of 8.1
Con Air - 1997 has a rating of 6.9
The Lion King - 1994 has a rating of 8.5
Interstellar - 2014 has a rating of 8.6

--- B: Gjennomsnittsrating ---
Gjennomsnittsrating for alle filmene: 8.16

--- C: Filmer fra og med 2010 ---
Inception - 2010 has a rating of 8.7
Inside Out - 2015 has a rating of 8.1
Interstellar - 2014 has a rating of 8.6

Process finished with exit code 0

"""