import file_handler as fih

filmer = [
    {"name":"Inception", "release":2010, "rating":8.7},
    {"name":"Inside Out", "release":2015, "rating":8.1},
    {"name":"Con Air", "release":1997, "rating":6.9}
    ]

def film_manager(f_list, mode="add", arg=None):

    def add():
        if isinstance(arg, list): # her kunne jeg gjort som jeg senere gjorde med change(), bare pakket en singel liste inn i en liste for å være konform med inputkravet
            if isinstance(arg[0], list):
                for movie in arg:
                    f_list.append({"name": movie[0], "release": movie[1], "rating": movie[2]})
                    print(f"{movie[0]} added successfully!")
                print()
                return

            f_list.append({"name": arg[0], "release": arg[1], "rating": arg[2]})
            print(f"{arg[0]} added successfully!\n")

        else:
            print(f"Arg is of wrong format.\nNeeds to be list or list of lists.\n")


    def remove():
        remove_m = {arg} if isinstance(arg, str) else set(arg) # [X1]
        for m in f_list:
            if m["name"] in remove_m:
                print(f"Removing {m['name']}\n")

        f_list[:] = [m for m in f_list if m["name"] not in remove_m]
        # [X1]:syntes min første metode var veldig kronglete så googlet etter en bedre løsning,
        # fant løsningen med å opprette ett set! Lar den gamle koden stå her så du kan se hva det startet som x)
        """
        internal_arg = arg
        if isinstance(internal_arg, str):
            internal_arg = [internal_arg]
        for r in internal_arg:
            for i, m in enumerate(cur_list):
                if r["name"] == m["name"]:
                    rm = cur_list.pop(i)
                    print(f"Removed {rm['name']}")
        """

    def change(): #var endel googling rundt denne for å finne metoder for å slanke ned operasjonene
        chg_arg = arg
        if isinstance(chg_arg[0], str): # denne er bare for å pakke det inn, så jeg kan bruke samme motor selv om det blir levert én liste, eller en liste med hundre
            chg_arg = [arg]

        chg_dict = {name: dict(kv_list) for name, kv_list in chg_arg}
        #chg_movies = [c[0] for c in chg_arg]
        for film in f_list:
            if film["name"] in chg_dict:
                film.update(chg_dict[film["name"]])

    def print_film():
        for film in f_list:
            print(f"{film['name']}, kom ut i {film['release']} og har en imdb rating på {film['rating']}")
        print()

    # moduser som kan brukes som argument i film_manager()
    modes = {
        "add": add,
        "remove": remove,
        "change": change,
        "print": print_film
    }
    modes[mode]()


# film_manager(list, mode, arg)
# list: list containing movie dictionaries: {"name":, "release":, "rating":}
# mode: what operation you want done; "add" (default), "remove", "change", "print"
# arg: additional arguments expected dependent on the mode:
#   "add": needs list or list of lists of movies, int the format ["name", "release", "rating"]
#   "remove": name of the movie or list with movie names; "name" or ["name1",...]
#   "change": List with lists with name, list of tuples with key, value pairs; ["name",[("key", value)]] or [[n,[(,),...]],[n,[(,),...]],....]
#   "print": no argument prints the whole list (might add more functionality later)

adding = [["Bicentennial Man",1999,6.9],["Galaxy Quest", 1999, 7.4],["The Man From Earth",2007,7.8],["Troll 2",1990,3.0]]
changes = ["Bicentennial Man",[("rating",9.0)]]


print("Adding:")
film_manager(filmer, "add", adding)
film_manager(filmer, "print")

print("Change:")
film_manager(filmer, "change", changes)
film_manager(filmer, "print")

print("Remove:")
film_manager(filmer, "remove", "Troll 2")
film_manager(filmer, "print")





#Bonus 3
test_liste1 = []
test_dict = filmer[4]
for film in filmer:
    test_liste1.append([film["name"], film["release"], film["rating"]])


print("Bonus 3:\nSkrive og lese til .txt")
print(f"Sender {test_liste1[0]} til lagring!")
fih.write_file(test_liste1[0], "mine_filmer.txt")
print(f"Output liste fra fil: {fih.read_file('mine filmer.txt')}")
print("\nSkrive og lese til .json")
fih.write_json(test_dict, "mine_filmer.json")
print(f"Output dict fra .json:\n{fih.read_json('mine_filmer.json')}")


"""
=============================================
Kjøreeksempel:
=============================================
Adding:
Bicentennial Man added successfully!
Galaxy Quest added successfully!
The Man From Earth added successfully!
Troll 2 added successfully!

Inception, kom ut i 2010 og har en imdb rating på 8.7
Inside Out, kom ut i 2015 og har en imdb rating på 8.1
Con Air, kom ut i 1997 og har en imdb rating på 6.9
Bicentennial Man, kom ut i 1999 og har en imdb rating på 6.9
Galaxy Quest, kom ut i 1999 og har en imdb rating på 7.4
The Man From Earth, kom ut i 2007 og har en imdb rating på 7.8
Troll 2, kom ut i 1990 og har en imdb rating på 3.0

Change:
Inception, kom ut i 2010 og har en imdb rating på 8.7
Inside Out, kom ut i 2015 og har en imdb rating på 8.1
Con Air, kom ut i 1997 og har en imdb rating på 6.9
Bicentennial Man, kom ut i 1999 og har en imdb rating på 9.0
Galaxy Quest, kom ut i 1999 og har en imdb rating på 7.4
The Man From Earth, kom ut i 2007 og har en imdb rating på 7.8
Troll 2, kom ut i 1990 og har en imdb rating på 3.0

Remove:
Removing Troll 2

Inception, kom ut i 2010 og har en imdb rating på 8.7
Inside Out, kom ut i 2015 og har en imdb rating på 8.1
Con Air, kom ut i 1997 og har en imdb rating på 6.9
Bicentennial Man, kom ut i 1999 og har en imdb rating på 9.0
Galaxy Quest, kom ut i 1999 og har en imdb rating på 7.4
The Man From Earth, kom ut i 2007 og har en imdb rating på 7.8

Bonus 3:
Skrive og lese til .txt
Sender ['Inception', 2010, 8.7] til lagring!
File mine_filmer.txt written
Output liste fra fil: ['Inception', 2010, 8.7]

Skrive og lese til .json
File mine_filmer.json written
Output dict fra .json:
{'name': 'Galaxy Quest', 'release': 1999, 'rating': 7.4}

Process finished with exit code 0
"""

