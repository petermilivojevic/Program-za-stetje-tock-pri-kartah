import bottle
from model import Stanje, Stetje, Igralec

SIFRIRNI_KLJUC = "To je poseben sifrirni kljuc iz predavanj"

def ime_uporabnikove_datoteke(uporabnisko_ime):
    return f"{uporabnisko_ime}.json"

def url_stetja(id_stetja):
    return f"/stetja/{id_stetja}/"

def stanje_trenutnega_uporabnika():
    uporabnisko_ime = bottle.request.get_cookie("uporabnisko_ime", secret=SIFRIRNI_KLJUC)
    if uporabnisko_ime == None:
        bottle.redirect("/prijava/")
    else:
        uporabnisko_ime = uporabnisko_ime
    ime_datoteke = ime_uporabnikove_datoteke(uporabnisko_ime)
    try:
        stanje = Stanje.preberi_iz_datoteke(ime_datoteke)
    except FileNotFoundError:
        stanje = Stanje(stetja=[])
        stanje.shrani_v_datoteko(ime_datoteke)
    return stanje

def shrani_stanje_trenutnega_uporabnika(stanje):
    uporabnisko_ime = bottle.request.get_cookie("uporabnisko_ime", secret=SIFRIRNI_KLJUC)
    ime_datoteke = ime_uporabnikove_datoteke(uporabnisko_ime)
    stanje.shrani_v_datoteko(ime_datoteke)

@bottle.get("/")
def zacetna_stran():
    stanje = stanje_trenutnega_uporabnika()
    return bottle.template(
        "zacetna_stran.tpl",
        stetja=stanje.stetja,
    )

@bottle.get("/zacetna_stran/")
def zacetna_stran_po_prijavi():
    stanje = stanje_trenutnega_uporabnika()
    return bottle.template(
        "stetja.tpl",
        stetja=stanje.stetja,
    )

@bottle.get("/prijava/")
def prijava_get():
    return bottle.template("prijava.tpl")

@bottle.post("/prijava/")
def prijava_post():
    uporabnisko_ime = bottle.request.forms.getunicode("uporabnisko_ime")
    geslo = bottle.request.forms.getunicode("geslo")
    if uporabnisko_ime == geslo:
        bottle.response.set_cookie("uporabnisko_ime", uporabnisko_ime, path="/", secret=SIFRIRNI_KLJUC)
        bottle.redirect("/zacetna_stran/")
    else:
        return "Napaka ob prijavi"



@bottle.get("/stetja/<id_stetja:int>/")
def prikazi_stetje(id_stetja):
    stanje = stanje_trenutnega_uporabnika()
    stetje = stanje.stetja[id_stetja]
    return bottle.template(
        "stetje.tpl",
        stetja=stanje.stetja,
        aktualno_stetje=stetje,
        id_aktualnega_stetja=id_stetja,
    )

@bottle.get("/dodaj_stetje/")
def dodaj_stetje_get():
    return bottle.template("dodaj_stetje.tpl", napake={}, polja={})

@bottle.post("/dodaj_stetje/")
def dodaj_stetje_post():
    stanje = stanje_trenutnega_uporabnika()
    ime = bottle.request.forms.getunicode("ime")
    stetje = Stetje(ime, igralci=[])
    napake = stanje.preveri_podatke_novega_stetja(ime)
    if napake:
        polja = {"ime": ime}
        return bottle.template("dodaj_stetje.tpl", napake=napake, polja=polja)
    else:
        id_stetja = stanje.dodaj_stetje(stetje)
        shrani_stanje_trenutnega_uporabnika(stanje)
        bottle.redirect(url_stetja(id_stetja))

@bottle.post("/stetja/<id_stetja:int>/")
def dodaj_igralca_post(id_stetja):
    stanje = stanje_trenutnega_uporabnika()
    stetje = stanje.stetja[id_stetja]
    ime = bottle.request.forms.getunicode("ime")
    if bottle.request.forms["tocke"]:
        tocke = bottle.request.forms["tocke"]
    else:
        tocke = ["0"]
    nov_igralec = Igralec(ime, tocke)
    stetje.dodaj_igralca(nov_igralec)
    shrani_stanje_trenutnega_uporabnika(stanje)
    bottle.redirect("/zacetna_stran/")




bottle.run(debug=True, reloader=True)