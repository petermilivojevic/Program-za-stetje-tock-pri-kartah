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


@bottle.get("/stetja/<id_stetja:int>/")
def prikazi_stetje(id_stetja):
    stanje = stanje_trenutnega_uporabnika()
    stetje = stanje.stetja[id_stetja]
    return bottle.template(
        "stetje.tpl",
        stetja=stanje.stetja,
        aktualno_stetje=stetje,
        id_aktualnega_stetja=id_stetja,
        napake={},
        polja={}
    )

@bottle.get("/stetja/<id_stetja:int>/<id_igralca:int>/")
def prikazi_igralca(id_stetja, id_igralca):
    stanje = stanje_trenutnega_uporabnika()
    stetje = stanje.stetja[id_stetja]
    igralec = stetje.igralci[id_igralca]
    return bottle.template(
        "stetje.tpl",
        stetja=stanje.stetja,
        aktualno_stetje=stetje,
        id_aktualnega_stetja=id_stetja,
        aktualni_igralec=igralec,
        id_aktualnega_igralca=id_igralca,
        napake={},
        polja={}
    )

@bottle.get("/dodaj_stetje/")
def dodaj_stetje_get():
    return bottle.template("dodaj_stetje.tpl", napake={}, polja={})

@bottle.post("/dodaj_stetje/")
def dodaj_stetje_post():
    stanje = stanje_trenutnega_uporabnika()
    ime = bottle.request.forms.getunicode("ime")
    stetje = Stetje(ime, igralci=[])
    napake = stanje.preveri_podatke_novega_stetja(stetje)
    if napake:
        polja = {"ime": ime}
        return bottle.template("dodaj_stetje.tpl", napake=napake, polja=polja)
    else:
        id_stetja = stanje.dodaj_stetje(stetje)
        shrani_stanje_trenutnega_uporabnika(stanje)
        bottle.redirect(url_stetja(id_stetja))

@bottle.post("/stetja/<id_stetja:int>/")
def dodaj_igralca(id_stetja):
    stanje = stanje_trenutnega_uporabnika()
    stetje = stanje.stetja[id_stetja]
    ime = bottle.request.forms.getunicode("ime")
    if bottle.request.forms.getunicode("tocke"):
        tocke = bottle.request.forms.getunicode("tocke")
    else:
        tocke = "0"
    nov_igralec = Igralec(ime, [tocke])
    napake = stetje.preveri_podatke_novega_igralca(nov_igralec)
    if napake:
        polja = {"ime": ime}
        return bottle.template(
            "stetje.tpl", 
            napake=napake, 
            polja=polja, 
            stetja=stanje.stetja, 
            aktualno_stetje=stetje, 
            id_aktualnega_stetja=id_stetja)
    else:
        stetje.dodaj_igralca(id_stetja, nov_igralec)
        shrani_stanje_trenutnega_uporabnika(stanje)
        bottle.redirect(url_stetja(id_stetja))

@bottle.post("/stetja/<id_stetja:int>/<id_igralca:int>/")
def dodaj_tocke(id_stetja, id_igralca):
    stanje = stanje_trenutnega_uporabnika()
    stetje = stanje.stetja[id_stetja]
    igralec = stetje.igralci[id_igralca]
    if bottle.request.forms.getunicode("nove_tocke"):
        tocke = bottle.request.forms.getunicode("nove_tocke")
    else:
        tocke = "0"
    igralec.dodaj_tocke(tocke)
    shrani_stanje_trenutnega_uporabnika(stanje)
    bottle.redirect(f"/stetja/{id_stetja}/{id_igralca}/")
    

@bottle.get("/stetja/<id_stetja:int>/<id_igralca:int>/")
def prikazi_stetje(id_stetja, id_igralca):
    stanje = stanje_trenutnega_uporabnika()
    stetje = stanje.stetja[id_stetja]
    igralec = stetje.igralci[id_igralca]
    return bottle.template(
        "stetje.tpl",
        stetja=stanje.stetja,
        aktualno_stetje=stetje,
        id_aktualnega_stetja=id_stetja,
        aktualni_igralec=igralec,
        id_aktualnega_igralca=id_igralca,
        napake={},
        polja={}
    )



bottle.run(debug=True, reloader=True)