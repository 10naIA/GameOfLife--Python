##
# I dette programmet skriver man inn to datoer (dag og måned), og så finner
# programmet ut hvilken dato som kommer først i året.
#

##
# Variablene defineres. Dag og måned i første dato legges sammen,
# deretter i den andre datoen.
#
print("Hva er den første datoen? Skriv først inn dag, så måned i tallformat.")
dag_1 = input("Dag: ")
måned_1 = input("Måned: ")
dato_1 = dag_1 + måned_1
print("Første dato:", dato_1)

print("Hva er den andre datoen? Skriv først inn dag, så måned i tallformat.")
dag_2 = input("Dag: ")
måned_2 = input("Måned: ")
dato_2 = dag_2 + måned_2
print("Andre dato:", dato_2)

##
# If/else-setningen skriver ut ulik tekst avhengig av om datoene er i
# riktig/feil rekkefølge, eller er samme dato. Elif brukes pga flere ledd i
# setningen.
#
if måned_1 + dag_1 < måned_2 + dag_2:
    print("Riktig rekkefølge!")
elif måned_1 + dag_1 == måned_2 + dag_2:
    print("Samme dato!")
else:
    print("Feil rekkefølge!")
