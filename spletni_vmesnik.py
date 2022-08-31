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
            id_aktualnega_stetja=id_stetja,
            )
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

@bottle.get("/stetja/<id_stetja:int>/pomoc_tarok/")
def pomoc_pri_stetju_tarok(id_stetja):
    stanje = stanje_trenutnega_uporabnika()
    stetje = stanje.stetja[id_stetja]
    return bottle.template(
        "pomoc_tarok.tpl",
        stetja=stanje.stetja,
        aktualno_stetje=stetje,
        id_aktualnega_stetja=id_stetja
    )

@bottle.get("/stetja/<id_stetja:int>/pomoc_enka/")
def pomoc_pri_stetju_enka(id_stetja):
    stanje = stanje_trenutnega_uporabnika()
    stetje = stanje.stetja[id_stetja]
    return bottle.template(
        "pomoc_enka.tpl",
        stetja=stanje.stetja,
        aktualno_stetje=stetje,
        id_aktualnega_stetja=id_stetja,
    )

@bottle.get("/stetja/<id_stetja:int>/pomoc_enka/porazenec/")
def pomoc_pri_stetju_enka(id_stetja):
    stanje = stanje_trenutnega_uporabnika()
    stetje = stanje.stetja[id_stetja]
    return bottle.template(
        "pomoc_enka_porazenec.tpl",
        stetja=stanje.stetja,
        aktualno_stetje=stetje,
        id_aktualnega_stetja=id_stetja,
    )

@bottle.get("/stetja/<id_stetja:int>/pomoc_enka/zmagovalec/")
def pomoc_pri_stetju_enka(id_stetja):
    stanje = stanje_trenutnega_uporabnika()
    stetje = stanje.stetja[id_stetja]
    return bottle.template(
        "pomoc_enka_zmagovalec.tpl",
        stetja=stanje.stetja,
        aktualno_stetje=stetje,
        id_aktualnega_stetja=id_stetja,
    )


@bottle.post("/stetja/<id_stetja:int>/<id_igralca:int>/pomoc_enka/porazenec/")
def dodaj_tocke_enka_porazenec(id_stetja, id_igralca):
    stanje = stanje_trenutnega_uporabnika()
    stetje = stanje.stetja[id_stetja]
    igralec = stetje.igralci[id_igralca]
    if bottle.request.forms.getunicode("stevilo enic"):
        tocke1 = bottle.request.forms.getunicode("stevilo enic")
    else:
        tocke1 = "0"
    if bottle.request.forms.getunicode("stevilo dvojic"):
        tocke2 = str(2*int(bottle.request.forms.getunicode("stevilo dvojic")))
    else:
        tocke2 = "0"
    if bottle.request.forms.getunicode("stevilo trojic"):
        tocke3 = str(3*int(bottle.request.forms.getunicode("stevilo trojic")))
    else:
        tocke3 = "0"
    if bottle.request.forms.getunicode("stevilo štiric"):
        tocke4 = str(4*int(bottle.request.forms.getunicode("stevilo stiric")))
    else:
        tocke4 = "0"
    if bottle.request.forms.getunicode("stevilo petic"):
        tocke5 = str(5*int(bottle.request.forms.getunicode("stevilo petic")))
    else:
        tocke5 = "0"
    if bottle.request.forms.getunicode("stevilo šestic"):
        tocke6 = str(6*int(bottle.request.forms.getunicode("stevilo sestic")))
    else:
        tocke6 = "0"
    if bottle.request.forms.getunicode("stevilo sedmic"):
        tocke7 = str(7*int(bottle.request.forms.getunicode("stevilo sedmic")))
    else:
        tocke7 = "0"
    if bottle.request.forms.getunicode("stevilo osmic"):
        tocke8 = str(8*int(bottle.request.forms.getunicode("stevilo osmic")))
    else:
        tocke8 = "0"
    if bottle.request.forms.getunicode("stevilo devetic"):
        tocke9 = str(9*int(bottle.request.forms.getunicode("stevilo devetic")))
    else:
        tocke9 = "0"
    if bottle.request.forms.getunicode("stevilo dvajsetic"):
        tocke20 = str(20*int(bottle.request.forms.getunicode("stevilo dvajsetic")))
    else:
        tocke20 = "0"
    if bottle.request.forms.getunicode("stevilo petdesetic"):
        tocke50 = str(50*int(bottle.request.forms.getunicode("stevilo petdesetic")))
    else:
        tocke50 = "0"
    if bottle.request.forms.getunicode("stevilo stotic"):
        tocke100 = str(100*int(bottle.request.forms.getunicode("stevilo stotic")))
    else:
        tocke100 = "0"
    karte = (tocke1, tocke2, tocke3, tocke4, tocke5, tocke6, tocke7, tocke8, tocke9, tocke20, tocke50, tocke100 )
    for tocke in karte:
        igralec.dodaj_tocke(tocke)
    shrani_stanje_trenutnega_uporabnika(stanje)
    bottle.redirect(f"/stetja/{id_stetja}/pomoc_enka/porazenec/")

@bottle.get("/stetja/<id_stetja:int>/<id_igralca:int>/pomoc_enka/zmagovalec/")
def dodaj_tocke_enka_zmagovalec_get(id_stetja, id_igralca):
    stanje = stanje_trenutnega_uporabnika()
    stetje = stanje.stetja[id_stetja]
    igralec = stetje.igralci[id_igralca]
    return bottle.template(
        "dodaj_tocke_zmagovalec.tpl",
        stetja=stanje.stetja,
        aktualno_stetje=stetje,
        id_aktualnega_stetja=id_stetja,
        aktualni_igralec=igralec,
        id_aktualnega_igralca=id_igralca,
    )

@bottle.post("/stetja/<id_stetja:int>/pomoc_enka/zmagovalec/")
def dodaj_tocke_enka_zmagovalec_post(id_stetja):
    igralec = bottle.request.forms.getunicode("zmagovalec")
    id_igralca =f"{igralec}"
    bottle.redirect(f"/stetja/{id_stetja}/{id_igralca}/pomoc_enka/zmagovalec/")

@bottle.post("/stetja/<id_stetja:int>/<id_igralca:int>/pomoc_enka/zmagovalec/")
def dodaj_tocke_enka_zmagovalec(id_stetja, id_igralca):
    stanje = stanje_trenutnega_uporabnika()
    stetje = stanje.stetja[id_stetja]
    igralec = stetje.igralci[id_igralca]
    if bottle.request.forms.getunicode("stevilo enic"):
        tocke1 = bottle.request.forms.getunicode("stevilo enic")
    else:
        tocke1 = "0"
    if bottle.request.forms.getunicode("stevilo dvojic"):
        tocke2 = str(2*int(bottle.request.forms.getunicode("stevilo dvojic")))
    else:
        tocke2 = "0"
    if bottle.request.forms.getunicode("stevilo trojic"):
        tocke3 = str(3*int(bottle.request.forms.getunicode("stevilo trojic")))
    else:
        tocke3 = "0"
    if bottle.request.forms.getunicode("stevilo štiric"):
        tocke4 = str(4*int(bottle.request.forms.getunicode("stevilo stiric")))
    else:
        tocke4 = "0"
    if bottle.request.forms.getunicode("stevilo petic"):
        tocke5 = str(5*int(bottle.request.forms.getunicode("stevilo petic")))
    else:
        tocke5 = "0"
    if bottle.request.forms.getunicode("stevilo šestic"):
        tocke6 = str(6*int(bottle.request.forms.getunicode("stevilo sestic")))
    else:
        tocke6 = "0"
    if bottle.request.forms.getunicode("stevilo sedmic"):
        tocke7 = str(7*int(bottle.request.forms.getunicode("stevilo sedmic")))
    else:
        tocke7 = "0"
    if bottle.request.forms.getunicode("stevilo osmic"):
        tocke8 = str(8*int(bottle.request.forms.getunicode("stevilo osmic")))
    else:
        tocke8 = "0"
    if bottle.request.forms.getunicode("stevilo devetic"):
        tocke9 = str(9*int(bottle.request.forms.getunicode("stevilo devetic")))
    else:
        tocke9 = "0"
    if bottle.request.forms.getunicode("stevilo dvajsetic"):
        tocke20 = str(20*int(bottle.request.forms.getunicode("stevilo dvajsetic")))
    else:
        tocke20 = "0"
    if bottle.request.forms.getunicode("stevilo petdesetic"):
        tocke50 = str(50*int(bottle.request.forms.getunicode("stevilo petdesetic")))
    else:
        tocke50 = "0"
    if bottle.request.forms.getunicode("stevilo stotic"):
        tocke100 = str(100*int(bottle.request.forms.getunicode("stevilo stotic")))
    else:
        tocke100 = "0"
    karte = (tocke1, tocke2, tocke3, tocke4, tocke5, tocke6, tocke7, tocke8, tocke9, tocke20, tocke50, tocke100 )
    for tocke in karte:
        igralec.dodaj_tocke(tocke)
    shrani_stanje_trenutnega_uporabnika(stanje)
    bottle.redirect(f"/stetja/{id_stetja}/{id_igralca}/pomoc_enka/zmagovalec/")






bottle.run(debug=True, reloader=True)