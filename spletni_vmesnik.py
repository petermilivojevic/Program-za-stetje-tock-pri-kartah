import bottle
from model import Stanje, Igralec


IME_DATOTEKE = "stanje.json"
try:
    stanje = Stanje.preberi_iz_datoteke(IME_DATOTEKE)
except FileNotFoundError:
    stanje = Stanje(igralci=[])


@bottle.get("/")
def zacetna_stran():
    return bottle.template(
        "zacetna_stran.tpl",
        igralci=stanje.igralci
    )


@bottle.get("/igralec/<id_igralca:int>/")
def prikazi_igralca(id_igralca):
    igralec=stanje.igralci[id_igralca]
    return bottle.template(
        "igralci.tpl",
        id_igralca=id_igralca,
        igralec=igralec
    )

    
bottle.run(debug=True, reloader=True)