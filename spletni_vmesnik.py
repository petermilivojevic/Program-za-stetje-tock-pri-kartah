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
        bottle.redirect("/")
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
        return "<h1>Napaka pri prijavi.</h1>"
    
@bottle.post("/odjava/")
def odjava_post():
    bottle.response.delete_cookie("uporabnisko_ime", path="/")
    bottle.redirect("/")

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

@bottle.get("/stetja/<id_stetja:int>/<id_igralca_ki_je_igral:int>/<id_zmagovalca:int>/pomoc_tarok/<stevilo_igralcev:int>/")
def kdo_je_zmagal(id_stetja, id_igralca_ki_je_igral, id_zmagovalca, stevilo_igralcev):
    stanje = stanje_trenutnega_uporabnika()
    stetje = stanje.stetja[id_stetja]
    st_igralcev = stetje.stevilo_igralcev()
    if st_igralcev == 2:
        if int(id_igralca_ki_je_igral) in range(st_igralcev):
            igralec = stetje.igralci[id_igralca_ki_je_igral]
        else:
            igralec = 2
    elif st_igralcev == 3:
        if int(id_igralca_ki_je_igral) in range(st_igralcev):
            igralec = stetje.igralci[id_igralca_ki_je_igral]
        else:
            igralec = 3
    
    return bottle.template(
        "pomoc_za_tarok.tpl",
        stetja=stanje.stetja,
        aktualno_stetje=stetje,
        id_aktualnega_stetja=id_stetja,
        aktualni_igralec=igralec,
        id_aktualnega_igralca=id_igralca_ki_je_igral,
        id_zmagovalca=id_zmagovalca,
        stevilo_igralcev=stevilo_igralcev
        )

@bottle.post("/stetja/<id_stetja:int>/<id_igralca_ki_je_igral:int>/<id_zmagovalca:int>/")
def dodaj_tocke_tarok_2(id_stetja, id_igralca_ki_je_igral, id_zmagovalca):
    stanje = stanje_trenutnega_uporabnika()
    stetje = stanje.stetja[id_stetja]
    igralec_ki_je_zmagal = stetje.igralci[id_zmagovalca]
    if int(id_igralca_ki_je_igral) < 2:
        igralec_ki_je_igral = stetje.igralci[id_igralca_ki_je_igral]
        if igralec_ki_je_igral == igralec_ki_je_zmagal:
            if bottle.request.forms.getunicode("nove_tocke"):
                tocke = str(2*int(bottle.request.forms.getunicode("nove_tocke")))
            else:
                tocke = "0"
            igralec_ki_je_igral.dodaj_tocke(tocke)
        else: 
            if bottle.request.forms.getunicode("nove_tocke"):
                tocke = str(-3*int(bottle.request.forms.getunicode("nove_tocke")))
            else:
                tocke = "0"
            igralec_ki_je_igral.dodaj_tocke(tocke)
    else:
        igralec_ki_je_igral = 2
        if id_zmagovalca == 0:
            porazenec = stetje.igralci[1]
            if bottle.request.forms.getunicode("nove_tocke"):
                tocke = bottle.request.forms.getunicode("nove_tocke")
            else:
                tocke = "0"
            tocke_porazenca = str(-1*int(tocke))
            igralec_ki_je_zmagal.dodaj_tocke(tocke)
            porazenec.dodaj_tocke(tocke_porazenca)
        else:
            porazenec = stetje.igralci[0]
            if bottle.request.forms.getunicode("nove_tocke"):
                tocke = bottle.request.forms.getunicode("nove_tocke")
            else:
                tocke = "0"
            tocke_porazenca = str(-1*int(tocke))
            igralec_ki_je_zmagal.dodaj_tocke(tocke)
            porazenec.dodaj_tocke(tocke_porazenca)
    shrani_stanje_trenutnega_uporabnika(stanje)
    bottle.redirect(url_stetja(id_stetja))

@bottle.post("/stetja/<id_stetja:int>/<id_aktualnega_igralca:int>/<id_zmagovalca:int>/pomoc_tarok/v_treh/dodatne_tocke/")
def dodaj_tocke_tarok_3(id_stetja, id_aktualnega_igralca, id_zmagovalca):
    stanje = stanje_trenutnega_uporabnika()
    stetje = stanje.stetja[id_stetja]
    if bottle.request.forms.getunicode("ime"):
        ime = int(bottle.request.forms.getunicode("ime"))
        igralec = stetje.igralci[ime]
    else:
        bottle.redirect(f"/stetja/{id_stetja}/{id_aktualnega_igralca}/{id_zmagovalca}/pomoc_tarok/3/")
    if bottle.request.forms.getunicode("kralj"):
        kralj = int(bottle.request.forms.getunicode("kralj"))
    else:
        kralj = 0
    if bottle.request.forms.getunicode("trula"):
        trula = int(bottle.request.forms.getunicode("trula"))
    else:
        trula = 0
    if bottle.request.forms.getunicode("pagat"):
        pagat = int(bottle.request.forms.getunicode("pagat"))
    else:
        pagat = 0
    if bottle.request.forms.getunicode("uspesen_kralj") and kralj == 20:
        u_k = int(bottle.request.forms.getunicode("uspesen_kralj"))
    else:
        u_k = 1
    if bottle.request.forms.getunicode("uspesna_trula") and trula == 20:
        u_t = int(bottle.request.forms.getunicode("uspesna_trula"))
    else:
        u_t = 1
    if bottle.request.forms.getunicode("uspesen_pagat") and pagat == 50:
        u_p = int(bottle.request.forms.getunicode("uspesen_pagat"))
    else:
        u_p = 1
    tocke = str(u_k*kralj + u_t*trula + u_p*pagat)
    igralec.dodaj_tocke(tocke)
    shrani_stanje_trenutnega_uporabnika(stanje)
    bottle.redirect(f"/stetja/{id_stetja}/{id_aktualnega_igralca}/{id_zmagovalca}/pomoc_tarok/3/")



@bottle.post("/stetja/<id_stetja:int>/<id_aktualnega_igralca:int>/<id_zmagovalca:int>/pomoc_tarok/v_treh/")
def dodaj_tocke_tarok_3(id_stetja, id_aktualnega_igralca, id_zmagovalca):
    stanje = stanje_trenutnega_uporabnika()
    stetje = stanje.stetja[id_stetja]
    igralec = stetje.igralci[id_aktualnega_igralca]
    if bottle.request.forms.getunicode("igra"):
        igra = bottle.request.forms.getunicode("igra")
        if bottle.request.forms.getunicode("nove_tocke"):
            vnesene_tocke = int(bottle.request.forms.getunicode("nove_tocke"))
        else:
            vnesene_tocke = -1
        if int(igra) < 5:
            tocke_igralca = vnesene_tocke - 35
        else:
            tocke_igralca = 0
        if igra == "1":
            tocke_igre = 10
        elif igra == "2":
            tocke_igre = 30
        elif igra == "3":
            tocke_igre = 50
        elif igra == "4":
            tocke_igre = 80
        elif igra == "5":
            tocke_igre = 70
        elif igra == "6":
            tocke_igre = 125
        elif igra == "7":
            tocke_igre = 150
        elif igra == "8":
            tocke_igre = 175
        elif igra == "9":
            tocke_igre = 250
        elif igra == "10":
            tocke_igre = 250
        elif igra == "11":
            tocke_igre = 300
        elif igra == "12":
            tocke_igre = 350
        elif igra == "13":
            tocke_igre = 500
        if int(igra) > 5 and vnesene_tocke != 70:
            tocke = str(tocke_igralca - tocke_igre)
        elif int(igra) == 5 and vnesene_tocke != 0:
            tocke = str(tocke_igralca - tocke_igre)
        else:
            tocke = str(tocke_igralca + tocke_igre)
        igralec.dodaj_tocke(tocke)
        shrani_stanje_trenutnega_uporabnika(stanje)
        bottle.redirect(f"/stetja/{id_stetja}/{id_aktualnega_igralca}/{id_zmagovalca}/pomoc_tarok/3/")
    else:
        bottle.redirect(f"/stetja/{id_stetja}/{id_aktualnega_igralca}/{id_zmagovalca}/pomoc_tarok/3/")



@bottle.post("/stetja/<id_stetja:int>/mondfang/")
def mondfang(id_stetja):
    stanje = stanje_trenutnega_uporabnika()
    stetje = stanje.stetja[id_stetja]
    if bottle.request.forms.getunicode("nesrecnez"):
        nesrecnez = bottle.request.forms.getunicode("nesrecnez")
        id_nesrecneza = int(f"{nesrecnez}")
        igralec = stetje.igralci[id_nesrecneza]
        tocke = "-21"
        igralec.dodaj_tocke(tocke)
    else:
        bottle.redirect(f"/stetja/{id_stetja}/pomoc_tarok/")
    shrani_stanje_trenutnega_uporabnika(stanje)
    bottle.redirect(f"/stetja/{id_stetja}/pomoc_tarok/")
    

@bottle.post("/stetja/<id_stetja:int>/<id_igralca_ki_je_igral:int>/pomoc_tarok/zmaga/")
def kdo_je_zmagal_tarok(id_stetja, id_igralca_ki_je_igral):
    stanje = stanje_trenutnega_uporabnika()
    stetje = stanje.stetja[id_stetja]
    zmagovalec = bottle.request.forms.getunicode("zmagovalec")
    id_zmagovalca = f"{zmagovalec}"
    st_igralcev = stetje.stevilo_igralcev()
    if bottle.request.forms.getunicode("zmagovalec"):
        if int(id_zmagovalca) in range(st_igralcev):
            bottle.redirect(f"/stetja/{id_stetja}/{id_igralca_ki_je_igral}/{id_zmagovalca}/pomoc_tarok/{st_igralcev}/")
    else:
        bottle.redirect(f"/stetja/{id_stetja}/{id_igralca_ki_je_igral}/2/pomoc_tarok/{st_igralcev}/")


@bottle.post("/stetja/<id_stetja:int>/pomoc_tarok/")
def kdo_je_igral(id_stetja):
    stanje = stanje_trenutnega_uporabnika()
    stetje = stanje.stetja[id_stetja]
    if bottle.request.forms.getunicode("igram"):
        igralec = bottle.request.forms.getunicode("igram")
        id_igralca = f"{igralec}"
        st_igralcev = stetje.stevilo_igralcev()
        if int(id_igralca) in range(st_igralcev):
            bottle.redirect(f"/stetja/{id_stetja}/{id_igralca}/2/pomoc_tarok/{st_igralcev}/")
        elif int(id_igralca) == st_igralcev:
            bottle.redirect(f"/stetja/{id_stetja}/2/2/pomoc_tarok/{st_igralcev}/")
    else:
        bottle.redirect(f"/stetja/{id_stetja}/pomoc_tarok/")


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
    if bottle.request.forms.getunicode("zmagovalec"):
        bottle.redirect(f"/stetja/{id_stetja}/{id_igralca}/pomoc_enka/zmagovalec/")
    else:
        bottle.redirect(f"/stetja/{id_stetja}/pomoc_enka/zmagovalec/")

@bottle.post("/stetja/<id_stetja:int>/<id_igralca:int>/pomoc_enka/zmagovalec/")
def dodaj_tocke_zmagovalcu_enka(id_stetja, id_igralca):
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