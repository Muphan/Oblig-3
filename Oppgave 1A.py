# sloppy AF, men gjør jobben.
# (Ja, jeg vet jeg bare kunne hardkoda det i 4 linjer eller noe.. men det er jo ikke noe gøy x))
# Kunne med fordel vært bygd som en klasse fra starten av.

student = {
    "first name": "Ola",
    "last name": "Nordmann",
    "favourite course": "Programmering 1"
}
commands = { # ser vel egentlig jeg kunne gjort dette vesentlig lettere med én funksjon, enn dette kommando-oppslagsverk-rælet her xP
        "first name": lambda: input("New first name?: ").strip(),               #.capitalize(),
        "last name": lambda: input("New last name?: ").strip(),                 #.capitalize(),
        "favourite course": lambda: input("New favourite course?: ").strip(),   #.capitalize(),
    }

def student_manager(mode, key=None, data=None): #bossman funksjon, delegerer til underfunksjoner basert på hva som skal gjøres

    def change_value():  #tar imot argumenter, eller spør hvis de ikke blir oppgitt i kallet
        nonlocal key, data
        if not key:
            for k in student.keys():
                print(f"{k}: {student.get(k)}")
            key = input("Please enter the key for the value you want to change: ")

        if key in commands:                     #sjekker om det finnes kommando for nøkkelen
            if data:                            #sjekker om dataen fulgte med kallet
                student.update({key: data})
            else:                               #hvis ikke kjører den kommandoen for å hente dataen
                student[key] = commands[key]()
        else:
            print("Key does not exist")

    def add_key():
        nonlocal key                            # måtte definere at vi jobber med den ytre variabelen key.
        if not(key):                            # sjekker om nøkkelen kom i kallet, hvis ikke spør den etter en
            key = input("Please enter the key you want to add: ")

        constructor = lambda k=key: input(f"New {k}?: ").strip()   # oppretter ny kommando..
        commands[key] = constructor                                # hele det oppslagsverket var strengt talt litt unnødvendig og overkill

        if data:
            student.update({key: data})      #sjekker om data kom med kallet
        else:
            student[key] = commands[key]()   #hvis ikke spør den etter data/value

    def print_key():       #en.. litt unnødvendig funksjon egentlig ---
        for k in data:
            print(f"{k.capitalize()}: {student[k]}")

    def return_key():      #  --- siden jeg så jeg skulle formatere det på en bestemt måte var det bedre å bare få verdien ut.
        ret_val =[]
        for k in data:
            ret_val.append(student[k])
        return ret_val


    modes = {                      #oppslagsverket for å kjøre sub-funksjoner
        "change": change_value,
        "add": add_key,
        "print": print_key,
        "return": return_key
    }

    return modes[mode]()

#student_manager("print",["first name", "last name"])
#student_manager("change", "first name")
#student_manager("change", "last name")

navn = student_manager("return", None, ["first name", "last name"])
print(f"{navn[0]} {navn[1]}")

student_manager("change","favourite course","ITF10219 Programmering 1")
#student_manager("print",None,["favourite course"])
student_manager("add","age",40)
student_manager("print",None,["first name", "last name", "age", "favourite course"])
#print(student)

#print(commands)


# ITF10219 Programmering 1


"""
=============================================
Kjøreeksempel:
=============================================

Ola Nordmann
New favourite course?: ITF10219 Programmering 1
Favourite course: ITF10219 Programmering 1
New age?: 40
First name: Ola
Last name: Nordmann
Age: 40
Favourite course: ITF10219 Programmering 1

Process finished with exit code 0


===========================================
Kjøreeksempel 2:
Definerer alt i kallene.
===========================================
Ola Nordmann
First name: Ola
Last name: Nordmann
Age: 40
Favourite course: ITF10219 Programmering 1

Process finished with exit code 0

"""