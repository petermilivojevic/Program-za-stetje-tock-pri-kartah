<h1>Dobrodošli na strani za dodajanje točk za enko po načinu za iskanje zmagovalca</h1>

<tbody>
    <tr>
        <h2>{{ aktualni_igralec.ime }}: {{ aktualni_igralec.vsota_tock() }} točk</h2>
        <form method="POST" action="/stetja/{{id_aktualnega_stetja}}/{{id_aktualnega_igralca}}/pomoc_enka/zmagovalec/">
            <p><input class="input is-small" type="number" step="1" min="0" max="8" name="stevilo enic" placeholder="krat 1"></p>
            <p><input class="input is-small" type="number" step="1" min="0" max="8" name="stevilo dvojic" placeholder="krat 2"></p>
            <p><input class="input is-small" type="number" step="1" min="0" max="8" name="stevilo trojic" placeholder="krat 3"></p>
            <p><input class="input is-small" type="number" step="1" min="0" max="8" name="stevilo stiric" placeholder="krat 4"></p>
            <p><input class="input is-small" type="number" step="1" min="0" max="8" name="stevilo petic" placeholder="krat 5"></p>
            <p><input class="input is-small" type="number" step="1" min="0" max="8" name="stevilo sestic" placeholder="krat 6"></p>
            <p><input class="input is-small" type="number" step="1" min="0" max="8" name="stevilo sedmic" placeholder="krat 7"></p>
            <p><input class="input is-small" type="number" step="1" min="0" max="8" name="stevilo osmic" placeholder="krat 8"></p>
            <p><input class="input is-small" type="number" step="1" min="0" max="8" name="stevilo devetic" placeholder="krat 9"></p>
            <p><input class="input is-small" type="number" step="1" min="0" max="24" name="stevilo dvajsetic" placeholder="krat 20"></p>
            <p><input class="input is-small" type="number" step="1" min="0" max="7" name="stevilo petdesetic" placeholder="krat 50"></p>
            <p><input class="input is-small" type="number" step="1" min="0" max="1" name="stevilo stotic" placeholder="krat 100"></p>
            <div class="control">
                <button class="button is-info is-small">dodaj točke</button>
            </div>
        </form>
    </tr>
</tbody>


<p>Dodali vse točke?<a href="/stetja/{{id_aktualnega_stetja}}/">Nazaj na štetje.</a></p>