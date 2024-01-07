##
# Denne klassen lager et rutenett fylt med celler, som kan oppdateres og tegnes, og teller antall generasjoner og levende celler.


# Importerer klassen Rutenett, og dermed ogsaa klassen Celle og randint.
from rutenett import Rutenett

# En verden inneholder alltid et rutenett (valgfri str) fylt med sammenkoblede celler. Starter paa generasjon null.
class Verden:
    def __init__(self, rader, kolonner):
        self._rutenett = Rutenett(rader, kolonner)
        self._generasjonsnummer = 0
        self._rutenett.fyll_med_tilfeldige_celler()
        self._rutenett.koble_celler()

    def str(self):
        return f"{self.tegn()}"

    # Antall levende celler printes i str-metoden i Rutenett. Hvis Rutenett.antall_levende kalles på i metoden under, printes
    # objektadressen! ** Feil: 'None' printes etter hvert rutenett! **
    def tegn(self):
        print(f"{self._rutenett} - Generasjon: {self._generasjonsnummer}")

    # Oppdaterer rutenett foer hver gang det tegnes. Faar da ny generasjon.
    def oppdatering(self):

        # Henter unoestet liste med alle celler i rutenettet. Teller levende naboer og oppdaterer om cellen er levende/doed ut
        # ifra det.
        liste = self._rutenett.hent_alle_celler()
        for celle in liste:
            celle.tell_levende_naboer()
            celle.oppdater_status()
        self._generasjonsnummer += 1
