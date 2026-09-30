filmer = [
    {"name":"Inception", "release":2010, "rating":8.7},
    {"name":"Inside Out", "release":2015, "rating":8.1},
    {"name":"Con Air", "release":1997, "rating":6.9}
    ]

def add_film(list, name, release, rating=5.0):
    list.append({"name":name, "release":release, "rating":rating})


add_film(filmer, "Bicentennial Man", 1999, 6.9) #krimminell lav score for denne filmen jeg ville gitt den nærmere 8!
add_film(filmer, "Galaxy Quest", 1999, 7.4)     # også undervurdert, ville gitt den 8.5-9
add_film(filmer, "The Man from Earth", 2007, 7.8)
add_film(filmer, "Troll 2", 1990) #denne har 3/10, en KLASSIKER! bør sees hvis du vil se latterlig dårlig film!

# A)
def print_films(list):
    for film in list:
        print(f"{film['name']} - {film['release']} has a rating of {film['rating']}")
    print()

print_films(filmer)

# B)
def avg_rating(list):
    rating_sum = 0
    for film in list:
        rating_sum += film["rating"]
    avg_score = rating_sum / len(list)
    return avg_score

print(f"Gjennomsnits rating: {avg_rating(filmer):.1f}\n")

# C)
def films_from(list, year):
    filtered_list = [f for f in list if f["release"] >= year]
    return filtered_list

print_films(films_from(filmer, 2010))


"""
=============================================
Kjøreeksempel:
=============================================
Inception - 2010 has a rating of 8.7
Inside Out - 2015 has a rating of 8.1
Con Air - 1997 has a rating of 6.9
Bicentennial Man - 1999 has a rating of 6.9
Galaxy Quest - 1999 has a rating of 7.4
The Man from Earth - 2007 has a rating of 7.8
Troll 2 - 1990 has a rating of 5.0

Gjennomsnits rating: 7.3

Inception - 2010 has a rating of 8.7
Inside Out - 2015 has a rating of 8.1


Process finished with exit code 0
"""


