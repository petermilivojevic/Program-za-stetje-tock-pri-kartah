<h1>Dobrodošli na strani za pomoč pri štetju točk za tarok</h1>

    % if aktualno_stetje.stevilo_igralcev() == 2:
        <h2> Tu je pomoč za igro v dveh.</h2>
        <p>Kdo je "igral"?<br></p>
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
    <h3>Način štetja</h3>
    <p>
        Če je igralec napovedal igro in jo zmagal dobi dvakratnik točk,
        ki si jih je priigral med igro. V kolikor je napovedano igro izgubil, se mu odšteje trikratnik točk,
        ki si jih je zmagovalec igre priigral.
    </p>
    <p>
        Če nihče ne napove igre se zmagovalcu prištejejo njegove priigrane točke in poražencu odštejejo zmagovlčeve priigrane točke.
    </p>

    

    % elif aktualno_stetje.stevilo_igralcev() == 3:
        <tr> Tu je pomoč za igro v treh.</tr>

    % elif aktualno_stetje.stevilo_igralcev() == 4:
        <tr> Tu je pomoč za igro v štirih.</tr>

    % else:
        <tr> Tarok se igra v dveh, treh, ali štirih</ tr>
    % end

<p><a href="/stetja/{{id_aktualnega_stetja}}/">Nazaj na štetje.</a></p>