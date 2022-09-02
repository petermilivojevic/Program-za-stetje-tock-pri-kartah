% rebase('osnova.tpl')

    % if aktualno_stetje.stevilo_igralcev() == 2:
        <strong> Tu je pomoč za igro v dveh.</strong><br>
        <strong><p>Kdo je "igral"?<br></p></strong>
        % for id_igralca, igralec in enumerate(aktualno_stetje.igralci):
    <tr>
        <form method="POST" action="/stetja/{{id_aktualnega_stetja}}/pomoc_tarok/">
            <td></td>
            <td>
                <input type="radio" name="igram" value="{{id_igralca}}">{{igralec.ime}}: {{ igralec.vsota_tock() }} trenutnih točk<br>
            </td>
        % end
            <td>
                <input type="radio" name="igram" value="2">Noben si ni želel "igrati"<br>
            </td>
            <div class="control">
                <button class="button is-info is-small">izberi</button>
            </div>
        </form>
    </tr>
   <br>
    <strong><p>Če se je zgodil "mondfang", izberite igralca, ki je izgubil monda?</p></strong>
    % for id_igralca, igralec in enumerate(aktualno_stetje.igralci):
    <tr>
        <form method="POST" action="/stetja/{{id_aktualnega_stetja}}/mondfang/">
            <td></td>
            <td>
                <input type="radio" name="nesrecnez" value="{{id_igralca}}">{{igralec.ime}}: {{ igralec.vsota_tock() }} trenutnih točk<br>
            </td>
    % end
            <div class="control">
                <button class="button is-info is-small">izberi</button>
            </div>
        </form>
    </tr>
<br>
    <strong>Način štetja</strong>
    <p>
        Če je igralec napovedal igro in jo zmagal dobi dvakratnik točk,
        ki si jih je priigral med igro. V kolikor je napovedano igro izgubil, se mu odšteje trikratnik točk,
        ki si jih je zmagovalec igre priigral.
    </p>
    <p>
        Če nihče ne napove igre se zmagovalcu prištejejo njegove priigrane točke in poražencu odštejejo zmagovlčeve priigrane točke.
    </p>

    

    % elif aktualno_stetje.stevilo_igralcev() == 3:
        <strong><p>Kdo je "igral"?<br></p></strong>
        % for id_igralca, igralec in enumerate(aktualno_stetje.igralci):
    <tr>
        <form method="POST" action="/stetja/{{id_aktualnega_stetja}}/pomoc_tarok/">
            <td></td>
            <td>
                <input type="radio" name="igram" value="{{id_igralca}}">{{igralec.ime}}: {{ igralec.vsota_tock() }} trenutnih točk<br>
            </td>
        % end
            <div class="control">
                <button class="button is-info is-small">izberi</button>
            </div>
        </form>
    </tr>
   <br>
    <strong><p>Če se je zgodil "mondfang", izberite igralca, ki je izgubil monda?</p></strong>
    % for id_igralca, igralec in enumerate(aktualno_stetje.igralci):
    <tr>
        <form method="POST" action="/stetja/{{id_aktualnega_stetja}}/mondfang/">
            <td></td>
            <td>
                <input type="radio" name="nesrecnez" value="{{id_igralca}}">{{igralec.ime}}: {{ igralec.vsota_tock() }} trenutnih točk<br>
            </td>
    % end
            <div class="control">
                <button class="button is-info is-small">izberi</button>
            </div>
        </form>
    </tr>
    <br>
    <br>
    <strong>Način štetja</strong>
        <p>trojka je vredna 10 točk + razlika</p>
        <p>dvojka je vredna 30 točk + razlika</p>
        <p>enka je vredna 50 točk + razlika</p>
        <p>solo brez talona je vreden 80 točk + razlika</p>
        <p>berač je vreden 70 točk</p>
        <p>tri - nap. barvni valat je vreden 125 točk</p>
        <p>dva - nap. barvni valat je vreden 150 točk</p>
        <p>ena - nap. barvni valat je vreden 175 točk</p>
        <p>brez - nap. barvni valat je vreden 250 točk</p>
        <p>tri - napovedani valat je vreden 250 točk</p>
        <p>dva - napovedani valat je vreden 300 točk</p>
        <p>ena - napovedani valat je vreden 350 točk</p>
        <p>brez talona - nap. valat je vreden 50 točk0 točk</p>
        <p>vsi kralji so vredni 10 točk (napovedani 20 točk)</p>
        <p>trula je vredna 10 točk (napovedana 20 točk)</p>
        <p>pagat ultimo je vreden 25 točk (napovedani je vreden 50 točk)</p>
        <p>nenapovedani valat je vreden 50 točk</p>
    

    % elif aktualno_stetje.stevilo_igralcev() == 4:
        <tr> Tu je pomoč za igro v štirih.</tr>

    % else:
        <tr> Tarok se igra v dveh, treh, ali štirih</ tr>
    % end
<br>
<br>
<p><a href="/stetja/{{id_aktualnega_stetja}}/">Nazaj na štetje.</a></p>