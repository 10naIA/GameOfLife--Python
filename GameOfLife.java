##
# Denne klassen lager en celle, og har metoder for aa se/oppdatere dens status (doed/levende), samt oppdatere antall levende
# naboceller.


# Hver celle starter som doed, og uten naboceller.
class Celle:
    def __init__(self):
        self._status = "doed"
        self._naboer = []
        self._ant_levende_naboer = 0

    # Viser '.' eller 'O' ut ifra om celle er doed/levende.
    def __str__(self):
        return f"{self.hent_status_tegn()}"

    # Endrer status til doed/levende.
    def sett_doed(self):
        self._status = "doed"

    def sett_levende(self):
        self._status = "levende"

    # Legger til nabo i cellens liste.
    def legg_til_nabo(self, nabo):
        self._naboer.append(nabo)

    def er_levende(self):
        if self._status == "levende":
            return True
        else:
            return False

    # Returnerer doed/levende.
    def hent_status(self):
        return self._status

    def hent_status_tegn(self):
        if self._status == "levende":
            return "O"
        else:
            return "."

    # Oppdaterer antall levende naboer.
    def tell_levende_naboer(self):
        for nabo in self._naboer:
            if nabo.er_levende():
                self._ant_levende_naboer += 1

    # Doed celle blir levende hvis 3 naboer. Levende celle doer hvis flere enn 3 eller faerre enn 2 naboer.
    def oppdater_status(self):
        if self._status == "doed" and self._ant_levende_naboer == 3:
            self.sett_levende()
        elif self._status == "levende" and self._ant_levende_naboer > 3 < 2:
            self.sett_doed()
