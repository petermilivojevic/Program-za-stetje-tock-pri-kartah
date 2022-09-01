% rebase('osnova.tpl')

<h1>Dobrodošli na strani za pomoč pri štetju točk za enko po načinu za iskanje zmagovalca</h1>

Kdo je zmagal?<br>
% for id_igralca, igralec in enumerate(aktualno_stetje.igralci):
    <tr>
        <form method="POST" action="/stetja/{{id_aktualnega_stetja}}/pomoc_enka/zmagovalec/">
            <td></td>
            <td>
                <input type="radio" name="zmagovalec" value="{{id_igralca}}">{{igralec.ime}}: {{ igralec.vsota_tock() }} trenutnih točk<br>
            </td>
            % end
            <div class="control">
                <button class="button is-info is-small">izberi</button>
            </div>
        </form>
    </tr>
<br>
<br>

<p><a href="/stetja/{{id_aktualnega_stetja}}/pomoc_enka/">Nazaj na stran za pomoč pri štetju za enko.</a></p>
<p><a href="/stetja/{{id_aktualnega_stetja}}/">Nazaj na štetje.</a></p>