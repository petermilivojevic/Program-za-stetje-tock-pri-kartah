
% if id_zmagovalca == 2:
Kdo je zmagal?<br>
% for id_igralca, igralec in enumerate(aktualno_stetje.igralci):
    <tr>
        <form method="POST" action="/stetja/{{id_aktualnega_stetja}}/{{id_aktualnega_igralca}}/pomoc_tarok/zmaga/">
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

% else:
Dodaj točke, ki si jih je med igro priigral zmagovalec.
<form method="POST" action="/stetja/{{id_aktualnega_stetja}}/{{id_aktualnega_igralca}}/{{id_zmagovalca}}/">
        <td></td> 
        <td>
            <input class="input is-small" type="number" step="1" min="36" max="71" name="nove_tocke" placeholder="dodaj točke">
        </td>
        <td>
        <div class="control">
            <button class="button is-info is-small">dodaj točke</button>
        </div>
    </td>
</form>
<p><a href="/stetja/{{id_aktualnega_stetja}}/{{id_aktualnega_igralca}}/2/pomoc_tarok/za_dva/">Nazaj na stran za izbiro zmagovalca.</a></p>

%end


%end
<p><a href="/stetja/{{id_aktualnega_stetja}}/pomoc_tarok/">Nazaj na stran za izbiro "igralca".</a></p>
<p><a href="/stetja/{{id_aktualnega_stetja}}/">Nazaj na štetje.</a></p>