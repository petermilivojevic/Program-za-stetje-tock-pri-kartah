<h1>Dobrodošli na strani za dodajanje točk za enko po načinu za iskanje zmagovalca</h1>

<tbody>
    <tr>
        <h2>{{ aktualni_igralec.ime }}: {{ aktualni_igralec.vsota_tock() }} točk</h2>
        <form method="POST" action="/stetja/{{id_aktualnega_stetja}}/{{id_aktualnega_igralca}}/pomoc_enka/zmagovalec/">
            <p><input class="input is-small" type="number" step="1" min="0" max="8" name="stevilo enic" placeholder="število enk"></p>
            <p><input class="input is-small" type="number" step="1" min="0" max="8" name="stevilo dvojic" placeholder="število dvojk"></p>
            <p><input class="input is-small" type="number" step="1" min="0" max="8" name="stevilo trojic" placeholder="število trojk"></p>
            <p><input class="input is-small" type="number" step="1" min="0" max="8" name="stevilo stiric" placeholder="število štirk"></p>
            <p><input class="input is-small" type="number" step="1" min="0" max="8" name="stevilo petic" placeholder="število petk"></p>
            <p><input class="input is-small" type="number" step="1" min="0" max="8" name="stevilo sestic" placeholder="število šestk"></p>
            <p><input class="input is-small" type="number" step="1" min="0" max="8" name="stevilo sedmic" placeholder="število sedemk"></p>
            <p><input class="input is-small" type="number" step="1" min="0" max="8" name="stevilo osmic" placeholder="število osemk"></p>
            <p><input class="input is-small" type="number" step="1" min="0" max="8" name="stevilo devetic" placeholder="število devetk"></p>
            <p><input class="input is-small" type="number" step="1" min="0" max="24" name="stevilo dvajsetic" placeholder="število preskoči, vzemi dve, zamenjaj smer"></p>
            <p><input class="input is-small" type="number" step="1" min="0" max="7" name="stevilo petdesetic" placeholder="število zamenjaj barvo, vzemi štiri"></p>
            <p><input class="input is-small" type="number" step="1" min="0" max="1" name="stevilo stotic" placeholder="število vzemi pet"></p>
            <div class="control">
                <button class="button is-info is-small">dodaj točke</button>
            </div>
        </form>
    </tr>
</tbody>


<p>Dodali vse točke?<a href="/stetja/{{id_aktualnega_stetja}}/">Nazaj na štetje.</a></p>