<h1>Dobrodošli na strani za pomoč pri štetju točk za enko po načinu za iskanje poraženca</h1>

<tbody>
    % for id_igralca, igralec in enumerate(aktualno_stetje.igralci):
    <tr>
        <p>{{ igralec.ime }}: {{ igralec.vsota_tock() }} točk</p>
        <form method="POST" action="/stetja/{{id_aktualnega_stetja}}/{{id_igralca}}/pomoc_enka/porazenec/">
            <td></td>
            <td>
                <input class="input is-small" type="number" step="1" min="0" max="8" name="stevilo enic" placeholder="število enk">
            </td>
            <td>
                <input class="input is-small" type="number" step="1" min="0" max="8" name="stevilo dvojic" placeholder="število dvojk">
            </td>
            <td>
                <input class="input is-small" type="number" step="1" min="0" max="8" name="stevilo trojic" placeholder="število trojk">
            </td>
            <td>
                <input class="input is-small" type="number" step="1" min="0" max="8" name="stevilo stiric" placeholder="število štirk">
            </td>
            <td>
                <input class="input is-small" type="number" step="1" min="0" max="8" name="stevilo petic" placeholder="število petk">
            </td>
            <td>
                <input class="input is-small" type="number" step="1" min="0" max="8" name="stevilo sestic" placeholder="število šestk">
            </td>
            <td>
                <input class="input is-small" type="number" step="1" min="0" max="8" name="stevilo sedmic" placeholder="število sedemk">
            </td>
            <td>
                <input class="input is-small" type="number" step="1" min="0" max="8" name="stevilo osmic" placeholder="število osemk">
            </td>
            <td>
                <input class="input is-small" type="number" step="1" min="0" max="8" name="stevilo devetic" placeholder="število devetk">
            </td>
            <td>
                <input class="input is-small" type="number" step="1" min="0" max="24" name="stevilo dvajsetic" placeholder="število preskoči, vzemi dve, zamenjaj smer">
            </td>
            <td>
                <input class="input is-small" type="number" step="1" min="0" max="7" name="stevilo petdesetic" placeholder="število zamenjaj barvo, vzemi štiri">
            </td>
            <td>
                <input class="input is-small" type="number" step="1" min="0" max="1" name="stevilo stotic" placeholder="število vzemi pet">
            </td>
            <td>
                <div class="control">
                    <button class="button is-info is-small">dodaj točke</button>
                </div>
            </td>
        </form>
    </tr>
% end    
</tbody>

<p>Dodali vse točke?<a href="/stetja/{{id_aktualnega_stetja}}/">Nazaj na stetje.</a></p>