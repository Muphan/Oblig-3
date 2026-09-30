
# A)
filmer = [
    {"name":"Inception", "release":2010, "rating":8.7},
    {"name":"Inside Out", "release":2015, "rating":8.1},
    {"name":"Con Air", "release":1997, "rating":6.9}
    ]

# B)+C)

def add_film(list, name, release, rating=5.0):
    list.append({"name":name, "release":release, "rating":rating})


add_film(filmer, "Bicentennial Man", 1999, 6.9) #krimminell lav score for denne filmen jeg ville gitt den nærmere 8!
add_film(filmer, "Galaxy Quest", 1999, 7.4)     # også undervurdert, ville gitt den 8.5-9
add_film(filmer, "The Man from Earth", 2007, 7.8)
add_film(filmer, "Troll 2", 1990) #denne har 3/10, en KLASSIKER! bør sees hvis du vil se latterlig dårlig film!

for film in filmer:
    print(f"{film['name']}, kom ut i {film['release']} og har en imdb rating på {film['rating']}")






"""
====================================
Kjøreeksempel:
====================================
Inception, kom ut i 2010 og har en imdb rating på 8.7
Inside Out, kom ut i 2015 og har en imdb rating på 8.1
Con Air, kom ut i 1997 og har en imdb rating på 6.9
Bicentennial Man, kom ut i 1999 og har en imdb rating på 6.9
Galaxy Quest, kom ut i 1999 og har en imdb rating på 7.4
The Man from Earth, kom ut i 2007 og har en imdb rating på 7.8
Troll 2, kom ut i 1990 og har en imdb rating på 5.0

Process finished with exit code 0
"""