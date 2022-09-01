% rebase('osnova.tpl')

<h1>Dobrodošli na strani za dodajanje točk za enko po načinu za iskanje zmagovalca</h1>

<tbody>
    <tr>
        <h2>{{ aktualni_igralec.ime }}: {{ aktualni_igralec.vsota_tock() }} točk</h2>
        <form method="POST" action="/stetja/{{id_aktualnega_stetja}}/{{id_aktualnega_igralca}}/pomoc_enka/zmagovalec/">
            <p><input class="input is-small" type="number" step="1" min="0" max="8" name="stevilo enic" placeholder="število kart s cifro 1"></p>
            <p><input class="input is-small" type="number" step="1" min="0" max="8" name="stevilo dvojic" placeholder="število kart s cifro 2"></p>
            <p><input class="input is-small" type="number" step="1" min="0" max="8" name="stevilo trojic" placeholder="število kart s cifro 3"></p>
            <p><input class="input is-small" type="number" step="1" min="0" max="8" name="stevilo stiric" placeholder="število kart s cifro 4"></p>
            <p><input class="input is-small" type="number" step="1" min="0" max="8" name="stevilo petic" placeholder="število kart s cifro 5"></p>
            <p><input class="input is-small" type="number" step="1" min="0" max="8" name="stevilo sestic" placeholder="število kart s cifro 6"></p>
            <p><input class="input is-small" type="number" step="1" min="0" max="8" name="stevilo sedmic" placeholder="število kart s cifro 7"></p>
            <p><input class="input is-small" type="number" step="1" min="0" max="8" name="stevilo osmic" placeholder="število kart s cifro 8"></p>
            <p><input class="input is-small" type="number" step="1" min="0" max="8" name="stevilo devetic" placeholder="število kart s cifro 9"></p>
            <p><input class="input is-small" type="number" step="1" min="0" max="24" name="stevilo dvajsetic" placeholder="število kart: vleci 2, zamenjaj smer, stop"></p>
            <p><input class="input is-small" type="number" step="1" min="0" max="7" name="stevilo petdesetic" placeholder="število kart: menjaj barvo, vleci 4"></p>
            <p><input class="input is-small" type="number" step="1" min="0" max="1" name="stevilo stotic" placeholder="plus 5"></p>
            <div class="control">
                <button class="button is-info is-small">dodaj točke</button>
            </div>
        </form>
    </tr>
</tbody>
<br>
<br>

<p><a href="/stetja/{{id_aktualnega_stetja}}/pomoc_enka/zmagovalec/">Nazaj na stran za izbiro zmagovalca.</a></p>
<p><a href="/stetja/{{id_aktualnega_stetja}}/pomoc_enka/">Nazaj na stran za pomoč pri štetju za enko.</a></p>
<p>Dodali vse točke?<a href="/stetja/{{id_aktualnega_stetja}}/">Nazaj na štetje.</a></p>