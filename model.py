import json

class Stanje:
    def __init__(self, stetja):
        self.stetja = stetja

    def dodaj_stetje(self, stetje):
        self.stetja.append(stetje)
        return len(self.stetja) - 1

    def preveri_podatke_novega_stetja(self, novo_stetje):
        for stetje in self.stetja:
            if stetje.ime == novo_stetje.ime:
                return {"ime": "Stetje s tem nazivom že obstaja"}

    def v_slovar(self):
        return {
            "stetje": [Stetje.v_slovar(stetje) for stetje in self.stetja],
        }

    @staticmethod
    def iz_slovarja(slovar):
        stanje = Stanje(
            [
                Stetje.iz_slovarja(stetje)
                for stetje in slovar["stetje"]
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
    

class Stetje:
    def __init__(self, ime, igralci):
        self.ime = ime
        self.igralci = igralci

    def stevilo_igralcev(self):
        return len(self.igralci)

    def dodaj_igralca(self, id_stetja, igralec):
        self.igralci.insert(id_stetja, igralec)

    def preveri_podatke_novega_igralca(self, nov_igralec):
        for igralec in self.igralci:
            if igralec.ime == nov_igralec.ime:
                return {"ime": "Igralec s tem imenom že obstaja"}

    def v_slovar(self):
            return {
                "ime": self.ime,
                "igralci": [ igralec.v_slovar() for igralec in self.igralci],
        }

    @staticmethod
    def iz_slovarja(slovar):
        return Stetje(
            slovar["ime"],
            [Igralec.iz_slovarja(sl_igralci) for sl_igralci in slovar["igralci"]]
        )


class Igralec:
    def __init__(self, ime, tocke):
        self.ime = ime
        self.tocke = tocke

    def dodaj_tocke(self, tocke_nove_igre):
        self.tocke.append(tocke_nove_igre)
    
    def vsota_tock(self):
        vsota = 0
        for tocke in self.tocke:
            vsota += int(tocke)
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



