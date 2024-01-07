##
# I dette programmet kan man svare på om man ønsker brus, og programmet skriver
# ut en tekst avhengig av svaret man gir.
#

svar = input("Vil du ha en brus? Svar ja/nei: ")

# Her svarer man "ja":
if svar == "ja":
    print("Her har du en brus!")

##
# Pga flere ledd i if/else-setningen brukes elif her.
# Her svarer man "nei".
#
elif svar == "nei":
    print("Den er grei.")

# Hvis man svarer noe annet enn ja eller nei forstår ikke programmet svaret.
else:
    print("Det forstod jeg ikke helt.")
