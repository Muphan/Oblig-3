"""
AI: Google Gemini
Prompt:
 Kan du lage en funksjon som tar imot 3 parametere, l, b, h, multipliserer disse og returnerer resultatet (volumet).
 gjerne legg til noen kall på slutten som kaller den
"""


def beregn_volum(l, b, h):
    """Beregner og returnerer volumet (l * b * h)."""
    return l * b * h


# Eksempelkall 1: Skrive ut direkte
volum_1 = beregn_volum(5, 3, 2)
print(f"Volum 1: {volum_1}")  # Utskrift: 30

# Eksempelkall 2: Bruke med desimaltall
volum_2 = beregn_volum(2.5, 4.0, 10.0)
print(f"Volum 2: {volum_2}")  # Utskrift: 100.0

# Eksempelkall 3: Bruk direkte i en print-setning
print(f"Volum 3: {beregn_volum(10, 10, 10)}")  # Utskrift: 1000


"""
====================================
Kjøreeksempel:
====================================
Volum 1: 30
Volum 2: 100.0
Volum 3: 1000

Process finished with exit code 0
"""