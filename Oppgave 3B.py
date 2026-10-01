"""
AI: Google Gemini
Prompt:
 Kan du lage en funksjon som tar imot en liste som parameter og skriver ut denne?

Legg også med en eksempel liste med 3 matretter som pirrer nysgjerrigheten til ditt neuralnet
"""

def skriv_ut_liste(elementer):
    """Tar imot en liste og skriver ut hvert element i konsollen."""
    for element in elementer:
        print(f"- {element}")


# Eksempelliste med retter som pirrer nysgjerrigheten til nevralnettet
nysgjerrige_matretter = [
    "Svart hvitløks-iskrem med krystallisert sjøtang",  # Kontrasten mellom fermentert umami og sødme/tekstur
    "Mole Poblano med 100 ingredienser og mørk sjokolade",  # Ekstremt kompleks kjemisk profil og smaksbalanse
    "Fugu (kulefisk) sashimi",  # Matematisk og presis spenning mellom kulinarisk kunst og presisjonsarbeid
]

# Kall på funksjonen
skriv_ut_liste(nysgjerrige_matretter)


"""
=============================================
Kjøreeksempel:
=============================================
- Svart hvitløks-iskrem med krystallisert sjøtang
- Mole Poblano med 100 ingredienser og mørk sjokolade
- Fugu (kulefisk) sashimi

Process finished with exit code 0

"""