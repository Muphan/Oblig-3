#Matet oppgave teksten direkte til gemini:
#Prompt: oppgaveteksten.

# 1. Oppretter dictionarien med informasjon om studenten
student = {
    "first name": "Ola",
    "last name": "Nordmann",
    "favourite course": "Programmering 1"
}

# 2. Skriver ut studentens fullstendige navn
print(f"{student['first name']} {student['last name']}")

# 3. Endrer favorittkurset programmatisk til å inkludere emnekoden
student["favourite course"] = "ITF10219 Programmering 1"

# 4. Legger programmatisk til en alder i dictionarien
student["age"] = 22

# Sjekker at alt ble oppdatert riktig
print(student)


"""
====================================
Kjøreeksempel:
====================================
Ola Nordmann
{'first name': 'Ola', 'last name': 'Nordmann', 'favourite course': 'ITF10219 Programmering 1', 'age': 22}

Process finished with exit code 0


"""