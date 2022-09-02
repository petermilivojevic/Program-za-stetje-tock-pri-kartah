% rebase('osnova.tpl')

<h1>Dobrodošli na strani za pomoč pri štetju točk za enko po načinu za iskanje poraženca</h1>

<tbody>
    % for id_igralca, igralec in enumerate(aktualno_stetje.igralci):
    <tr>
        <p>{{ igralec.ime }}: {{ igralec.vsota_tock() }} točk</p>
        <form method="POST" action="/stetja/{{id_aktualnega_stetja}}/{{id_igralca}}/pomoc_enka/porazenec/">
            <td></td>
            <td>
                <input class="input is-small" type="number" step="1" min="0" max="8" name="stevilo enic" placeholder="število kart s cifro 1">
            </td>
            <td>
                <input class="input is-small" type="number" step="1" min="0" max="8" name="stevilo dvojic" placeholder="število kart s cifro 2">
            </td>
            <td>
                <input class="input is-small" type="number" step="1" min="0" max="8" name="stevilo trojic" placeholder="število kart s cifro 3">
            </td>
            <td>
                <input class="input is-small" type="number" step="1" min="0" max="8" name="stevilo stiric" placeholder="število kart s cifro 4">
            </td>
            <td>
                <input class="input is-small" type="number" step="1" min="0" max="8" name="stevilo petic" placeholder="število kart s cifro 5">
            </td>
            <td>
                <input class="input is-small" type="number" step="1" min="0" max="8" name="stevilo sestic" placeholder="število kart s cifro 6">
            </td>
            <td>
                <input class="input is-small" type="number" step="1" min="0" max="8" name="stevilo sedmic" placeholder="število kart s cifro 7">
            </td>
            <td>
                <input class="input is-small" type="number" step="1" min="0" max="8" name="stevilo osmic" placeholder="število kart s cifro 8">
            </td>
            <td>
                <input class="input is-small" type="number" step="1" min="0" max="8" name="stevilo devetic" placeholder="število kart s cifro 9">
            </td>
            <td>
                <input class="input is-small" type="number" step="1" min="0" max="24" name="stevilo dvajsetic" placeholder="število kart: vleci 2, zamenjaj smer, stop">
            </td>
            <td>
                <input class="input is-small" type="number" step="1" min="0" max="7" name="stevilo petdesetic" placeholder="število kart: menjaj barvo, vleci 4">
            </td>
            <td>
                <input class="input is-small" type="number" step="1" min="0" max="1" name="stevilo stotic" placeholder="karta plus 5">
            </td>
            <td>
                <div class="control">
                    <button class="button is-info is-small">dodaj točke</button>
                </div>
            </td>
            <br>
        </form>
    </tr>
% end    
</tbody>
<br>

<p><a href="/stetja/{{id_aktualnega_stetja}}/pomoc_enka/">Nazaj na stran za pomoč pri štetju za enko.</a></p>
<p>Dodali vse točke?<a href="/stetja/{{id_aktualnega_stetja}}/">Nazaj na stetje.</a></p>