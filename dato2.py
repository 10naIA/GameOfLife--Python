##
# I dette programmet skriver man inn to datoer (dag og måned), og så finner
# programmet ut hvilken dato som kommer først i året.
#

##
# Variablene defineres. Man skriver måned først fordi dag først vil gi et for
# høyt heltall, slik at programmet misforstår.
#
print("Hva er den første datoen? Skriv i formatet MMDD.")
dato_1 = input("Dato: ")
print("Første dato:", dato_1)

print("Hva er den andre datoen? Skriv i formatet MMDD.")
dato_2 = input("Dato: ")
print("Andre dato:", dato_2)

##
# If/else-setningen skriver ut ulik tekst avhengig av om datoene er i
# riktig/feil rekkefølge, eller er samme dato. Elif brukes pga flere ledd.
#
if dato_1 < dato_2:
    print("Riktig rekkefølge!")
elif dato_1 == dato_2:
    print("Samme dato!")
else:
    print("Feil rekkefølge!")
