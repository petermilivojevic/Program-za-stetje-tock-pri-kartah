% rebase('osnova.tpl')

% if stevilo_igralcev == 2:
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
                <input class="input is-small" type="number" step="1" min="36" max="70" name="nove_tocke" placeholder="dodaj točke">
            </td>
            <td>
            <div class="control">
                <button class="button is-info is-small">dodaj točke</button>
            </div>
        </td>
    </form>
    <br>
    <p><a href="/stetja/{{id_aktualnega_stetja}}/{{id_aktualnega_igralca}}/2/pomoc_tarok/2/">Nazaj na stran za izbiro zmagovalca.</a></p>

    %end

% elif stevilo_igralcev == 3:
    % if aktualni_igralec:
    <thead>
        <strong>Kako je igral?</strong><br>
        <tr>
            <form method="POST" action="/stetja/{{id_aktualnega_stetja}}/{{id_aktualnega_igralca}}/{{id_zmagovalca}}/pomoc_tarok/v_treh/">
                <td>
                    <div class="control">
                        <input type="radio" name="igra" value="1">trojka<br>
                        <input type="radio" name="igra" value="2">dvojka<br>
                        <input type="radio" name="igra" value="3">enka<br>
                        <input type="radio" name="igra" value="4">brez talona<br>
                        <input type="radio" name="igra" value="5">berač<br>
                        <input type="radio" name="igra" value="6">tri - nap. barvni valat<br>
                        <input type="radio" name="igra" value="7">dva - nap. barvni valat<br>
                        <input type="radio" name="igra" value="8">ena - nap. barvni valat<br>
                        <input type="radio" name="igra" value="9">brez - nap. barvni valat<br>
                        <input type="radio" name="igra" value="10">tri - napovedani valat<br>
                        <input type="radio" name="igra" value="11">dva - napovedani valat<br>
                        <input type="radio" name="igra" value="12">ena - napovedani valat<br>
                        <input type="radio" name="igra" value="13">brez talona - nap. valat<br>
                    </div>
                </td>
                <td>
                    <input class="input is-small" type="number" step="1" min="0" max="70" name="nove_tocke" placeholder="dodaj točke">
                </td>
                Če ste izbrali eno izmed zgornjih 4 izbir vnesite točke, ki si jih je "igralec" med igro priigral.<br>
                V kolikor ste izbrali berača vpišite 0 če je "igralec" zmagal.<br>
                Če ste izbrali izbiro z napovedjo valata vpišite 70 v kolikor je "igralec" uresničil napoved.

                <div class="control">
                    <button class="button is-info is-small">potrdi</button>
                </div>
            </form>
        </tr>
        <br>
        <br>
        <tr>
            <form method="POST" action="/stetja/{{id_aktualnega_stetja}}/{{id_aktualnega_igralca}}/{{id_zmagovalca}}/pomoc_tarok/v_treh/dodatne_tocke/">
                <td>
                    <div class="control">
                    <strong>Izberite igralc, ki je napovedoval.</strong><br>
                    % for id_igralca, igralec in enumerate(aktualno_stetje.igralci):
                        <td>
                            <input type="radio" name="ime" value="{{id_igralca}}">{{igralec.ime}}: {{ igralec.vsota_tock() }} trenutnih točk<br>
                        </td>
                    %end
                        <strong>Izberite kaj je izbrani igralec napovedal za kralje.</strong><br>
                        <div class="control">
                            <input type="radio" name="kralj" value="20">napovedani kralji<br>
                            <input type="radio" name="kralj" value="10">ne napovedani kralji<br>
                            <input type="radio" name="kralj" value="0">ni bilo napovedi<br>
                            <div class="control">
                                <input type="checkbox" name="uspesen_kralj" value="-1">napoved ni bila uspešna<br>
                            </div>
                        </div>
                        <strong>Izberite kaj je izbrani igralec napovedal za trulo.</strong><br>
                        <div class="control">
                            <input type="radio" name="trula" value="20">napovedana trula<br>
                            <input type="radio" name="trula" value="10">ne napovedana trula<br>
                            <input type="radio" name="trula" value="0">ni bilo napovedi<br>
                            <div class="control">
                                <input type="checkbox" name="uspesna_trula" value="-1">napoved ni bila uspešna<br>
                            </div>
                        </div>
                        <strong>Izberite kaj je izbrani igralec napovedal za pagat ultimo.</strong><br>
                        <div class="control">
                            <input type="radio" name="pagat" value="50">napovedani pagat ultimo<br>
                            <input type="radio" name="pagat" value="25">ne napovedani pagat ultimo<br>
                            <input type="radio" name="pagat" value="0">ni bilo napovedi<br>
                            <div class="control">
                                <input type="checkbox" name="uspesen_pagat" value="-1">napoved ni bila uspešna<br>
                            </div>
                        </div>
                        <div class="control">
                            <button class="button is-info is-small">potrdi</button>
                        </div>
                    </div>
                </td>
            </form>
        </tr>
    </thead>
<br>
%end
%end
<p><a href="/stetja/{{id_aktualnega_stetja}}/pomoc_tarok/">Nazaj na stran za izbiro "igralca".</a></p>
<p><a href="/stetja/{{id_aktualnega_stetja}}/">Nazaj na štetje.</a></p>