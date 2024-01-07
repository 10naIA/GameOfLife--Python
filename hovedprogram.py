##
# Hovedprogrammet lar bruker lage et ferdig rutenett av valgfri str, og oppdatere og tegne det uendelig mange ganger.

# Importerer klassen Verden.
from verden import Verden

def hovedprogram():
    # Tester programmet ved aa tegne et tilfeldige brett, og 5 generasjoner av dette. Har gjentatt dette mange ganger, og funker
    # bra i hvert fall for 'still lives', da både 'block' og 'tub' forblir uforandret. Litt mer usikker paa andre moenstre.

    test_verden = Verden(5, 5)
    test_verden.tegn()
    for i in range(5):
        test_verden.oppdatering()
        test_verden.tegn()

    # Lar bruker legge inn dimensjonene til et rutenett.
    rad_input = int(input("Skriv in rad-dimensjonen i tallformat: "))
    kol_input = int(input("Skriv inn kolonne-dimensjonen i tallformat: "))

    # Lager og tegner Verden-objekt med inputene.
    verden = Verden(rad_input, kol_input)
    verden.tegn()
    # Avslutter loop hvis input er 'q'.
    fortsett = input("Press enter for aa fortsette. Skriv inn q og trykk enter for aa avslutte: ")
    while fortsett != "q":
        verden.oppdatering()
        verden.tegn()
        fortsett = input("Press enter for aa fortsette. Skriv inn q og trykk enter for aa avslutte: ")


# Starter hovedprogrammet.
hovedprogram()
