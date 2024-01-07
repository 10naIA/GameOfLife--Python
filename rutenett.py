##
# Denne klassen lager et rutenett som man kan fylle med celler og legge til deres naboer, samt telle antall levende celler.
# Rutenettet kan ogsaa tegnes.

# Importerer modul for å bruke tilfeldige tall senere, samt klassen Celle.
from random import randint
from celle import Celle

# Et rutenett har valgfritt antall rader og kolonner, og starter uten celler.
class Rutenett:
    def __init__(self, rader, kolonner):
        self._ant_rader = rader
        self._ant_kolonner = kolonner
        self._rutenett = self._lag_tomt_rutenett()

    # Metoden brukes for leselig utskrift av rutenettet, samt antall levende celler, i klassen Verden.
    def __str__(self):
        return f"{self.tegn_rutenett()}\nAntall levende celler: {self.antall_levende()}"

    # Lager tomt rutenett
    def _lag_tomt_rutenett(self):
        tomt_rutenett = []
        teller = 0

        # Lager 1 rad per loop, og legger til i rutenettet. Repeterer loopen like mange ganger som oensket antall rader.
        while teller < self._ant_rader:
            rad = self._lag_tom_rad()
            tomt_rutenett.append(rad)
            teller += 1

        # Returnerer liste, ellers kommer feilmld i testprogrammet.
        return tomt_rutenett

    # Lager 1 tom rad-liste ut ifra oensket antall kolonner. Hvert element er None.
    def _lag_tom_rad(self):
        rad_liste = []
        teller = 0
        while teller < self._ant_kolonner:
            rad_liste.append(None)
            teller += 1
        return rad_liste

    # Itererer gjennom rutenettet( foerst rad, saa cellene i raden) og erstatter None med ny celle.
    def fyll_med_tilfeldige_celler(self):
        for rad in range(self._ant_rader):
            for kol in range(self._ant_kolonner):
                self.lag_celle(rad, kol)

    # Bruker randint for aa velge tilfeldige tall. 1/3-sjanse for at en nylaget celle er levende.
    def lag_celle(self, rad, kol):
        celle = Celle()
        tilstand = randint(0, 2)
        if tilstand == 2:
            celle.sett_levende()

        # Legges i rutenettet paa oppgitt plass.
        self._rutenett[rad][kol] = celle

    # Henter celle paa oppgitt plass hvis plassen er innenfor rekkevidden.
    def hent_celle(self, rad, kol):
        if rad in range(0, self._ant_rader) and kol in range(0, self._ant_kolonner):
            return self._rutenett[rad][kol]

    # Tegner rutenettet.
    def tegn_rutenett(self):
        print("\n"*5)
        for rad in self._rutenett:
            # Printer linjeskift etter hver rad, ellers kommer alt paa samme linje.
            print()
            for kol in rad:
                # Fjerner linjeskift for aa faa én rad per linje.
                print(kol, end="")
        print()

    # Henter celle paa oppgitte koordinater, og finner naboer. Celle med naboer paa alle kanter, har totalt 8 stk.
    def _sett_naboer(self, rad, kol):
        cellen = self.hent_celle(rad, kol)

        # Trekker fra/legger til 1 paa oppgitte koordinater, og hvis gyldig celle paa denne plassen legges den i nabolisten til
        # cellen.
        if self.hent_celle(rad-1, kol-1) is not None:
            cellen.legg_til_nabo(self.hent_celle(rad-1, kol-1))
        if self.hent_celle(rad-1, kol) is not None:
            cellen.legg_til_nabo(self.hent_celle(rad-1, kol))
        if self.hent_celle(rad-1, kol+1) is not None:
            cellen.legg_til_nabo(self.hent_celle(rad-1, kol+1))
        if self.hent_celle(rad, kol-1) is not None:
            cellen.legg_til_nabo(self.hent_celle(rad, kol-1))
        if self.hent_celle(rad, kol+1) is not None:
            cellen.legg_til_nabo(self.hent_celle(rad, kol+1))
        if self.hent_celle(rad+1, kol-1) is not None:
            cellen.legg_til_nabo(self.hent_celle(rad+1, kol-1))
        if self.hent_celle(rad+1, kol) is not None:
            cellen.legg_til_nabo(self.hent_celle(rad+1, kol))
        if self.hent_celle(rad+1, kol+1) is not None:
            cellen.legg_til_nabo(self.hent_celle(rad+1, kol+1))

    # Kobler alle cellene i rutenettet, ved å gi alle naboer, med metoden over.
    def koble_celler(self):
        for rad in range(self._ant_rader):
            for kol in range(self._ant_kolonner):
                self._sett_naboer(rad, kol)

    # Returnerer unoestet liste med celler fra rutenettet.
    def hent_alle_celler(self):
        celleListe = []
        for rad in self._rutenett:
            for celle in rad:
                celleListe.append(celle)
        return celleListe

    # Itererer gjennom unoestet liste, og teller antall levende celler. Returnerer tallet.
    def antall_levende(self):
        teller = 0
        celleListe = self.hent_alle_celler()
        for celle in celleListe:
            if celle.er_levende():
                teller += 1
        return teller
