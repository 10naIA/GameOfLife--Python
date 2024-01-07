##
# Dette programmet lar en skrive inn navnet sitt, og skriver ut velkomsthilsen,
# alder, antall fag og differansen. Et nytt navn legges til det første, og
# resultatet skrives ut.
#

print("Hei Student!")
navn = input("Oppgi navnet ditt: ")
print("Hei", navn)

##
# Alder og antall fag dette semesteret får en verdi, differansen kalkuleres,
# og alt skrives ut.
#
alder = 20
antall_fag = 3
print("Alder: ", alder)
print("Antall fag: ", antall_fag)

differanse = 20 - 3
print("Differanse: ", differanse)

# Ber bruker om å oppgi et nytt navn, så slås begge navnene sammen.
nytt_navn = input("Oppgi et nytt navn: ")
sammen = navn + nytt_navn
print(sammen)

##
# Den forrige variabelen endres, og navnene får mellomrom og "og" mellom seg.
# Endringen printes ikke ut siden oppgaven ikke krever det.
#
sammen = navn + (" og ") + nytt_navn
