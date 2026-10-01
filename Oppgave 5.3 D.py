"""
AI: Google Gemini
Prompt:
Utvid forrige oppgave med noen funksjoner og benytt dem i koden din.
A) Opprett en funksjon som tar en liste med filmer, og filnavn som parameter.
Benytt denne funksjonen til å skrive alle filmene i lista til en fil du selv velger navnet på f.eks.
"movies.txt". Hvis filen allerede eksisterer, skal den overskrives.
Legg gjerne til hver film som en egen linje i filen med et fint format. For eksempel:

The Lion King - 1994 has a rating of 8.5

B) Lag en funksjon som leser den samme filen (filnavn som input-parameter til funksjonen)
og skriver ut innholdet til terminalen.
"""

# Oppretter filmlisten
movies = [
    {"name": "The Matrix", "year": 1999, "rating": 8.7},
    {"name": "Terminator 2: Judgment Day", "year": 1991, "rating": 8.6},
    {"name": "2001: A Space Odyssey", "year": 1968, "rating": 8.3},
    {"name": "WALL-E", "year": 2008, "rating": 8.4},
    {"name": "Ex Machina", "year": 2014, "rating": 7.7},
    {"name": "Her", "year": 2013, "rating": 8.0},
    {"name": "I, Robot", "year": 2004, "rating": 7.1},
    {"name": "Blade Runner 2049", "year": 2017, "rating": 8.0},
    {"name": "A.I. Artificial Intelligence", "year": 2001, "rating": 7.2},
    {"name": "Upgrade", "year": 2018, "rating": 7.5}
]
## Hmm.. ser ut som gemini har sans for ett spesielt tema... (... okei... I *MAY* have nudged it a bit.. :3)

# A) Funksjon som skriver filmlisten til fil (overskriver dersom den finnes)
def write_movies_to_file(movie_list, filename):
    # 'w'-modus sørger for at filen overskrives hvis den allerede eksisterer
    with open(filename, "w", encoding="utf-8") as file:
        for movie in movie_list:
            line = f"{movie['name']} - {movie['year']} has a rating of {movie['rating']}\n"
            file.write(line)
    print(f"Filmene ble vellykket skrevet til '{filename}'.")


# B) Funksjon som leser filen og skriver ut innholdet til terminalen
def read_movies_from_file(filename):
    print(f"\n--- Innhold fra '{filename}' ---")
    try:
        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                # .strip() fjerner linjeskiftet (\n) på slutten av hver linje
                print(line.strip())
    except FileNotFoundError:
        print(f"Feil: Filen '{filename}' ble ikke funnet.")


# --- TESTING AV FUNKSJONENE ---

# A: Skriver filmene til filen "movies.txt"
write_movies_to_file(movies, "AI movies.txt")

# B: Leser og skriver ut filen til konsollen
read_movies_from_file("AI movies.txt")


"""
=============================================
Kjøreeksempel:
=============================================
Filmene ble vellykket skrevet til 'AI movies.txt'.

--- Innhold fra 'AI movies.txt' ---
The Matrix - 1999 has a rating of 8.7
Terminator 2: Judgment Day - 1991 has a rating of 8.6
2001: A Space Odyssey - 1968 has a rating of 8.3
WALL-E - 2008 has a rating of 8.4
Ex Machina - 2014 has a rating of 7.7
Her - 2013 has a rating of 8.0
I, Robot - 2004 has a rating of 7.1
Blade Runner 2049 - 2017 has a rating of 8.0
A.I. Artificial Intelligence - 2001 has a rating of 7.2
Upgrade - 2018 has a rating of 7.5

Process finished with exit code 0
"""