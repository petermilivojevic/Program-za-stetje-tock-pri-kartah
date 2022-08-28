import json

class Stanje:
    def __init__(self, igralci):
        self.igralci = igralci

    def dodaj_igralca(self, igralec):
        self.igralci.append(igralec)

    def preveri_podatke_novega_igralca(self, nov_igralec):
        for igralec in self.igralci:
            if igralec.ime == nov_igralec.ime:
                return {"ime": "Igralec s tem imenom že obstaja"}

    def v_slovar(self):
        return {
            "igralci": [igralec.v_slovar() for igralec in self.igralci],
        }

    @staticmethod
    def iz_slovarja(slovar):
        stanje = Stanje(
            [
                Igralec.iz_slovarja(sl_igralci)
                for sl_igralci in slovar["igralci"]
            ]
        )
        return stanje

    def shrani_v_datoteko(self, ime_datoteke):
        with open(ime_datoteke, "w") as dat:
            slovar = self.v_slovar()
            json.dump(slovar, dat, indent=4, ensure_ascii=False)

    @staticmethod
    def preberi_iz_datoteke(ime_datoteke):
        with open(ime_datoteke) as dat:
            slovar = json.load(dat)
            return Stanje.iz_slovarja(slovar)


class Igralec:
    def __init__(self, ime, tocke):
        self.ime = ime
        self.tocke = tocke

    def dodaj_tocke(self, tocke_nove_igre):
        self.tocke.append(tocke_nove_igre)
    
    def vsota_tock(self):
        vsota = 0
        for element in self.tocke:
            vsota += int(element)
        return vsota

    def v_slovar(self):
        return {
            "ime": self.ime,
            "tocke": self.tocke,
        }

    @staticmethod
    def iz_slovarja(slovar):
        return Igralec(
            slovar["ime"],
            slovar["tocke"],
        )



