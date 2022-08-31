<h1>Dobrodošli na strani za pomoč pri štetju točk za tarok</h1>

    % if aktualno_stetje.stevilo_igralcev() == 2:
        <tr> Tu je pomoč za igro v dveh.</tr>

    % elif aktualno_stetje.stevilo_igralcev() == 3:
        <tr> Tu je pomoč za igro v treh.</tr>

    % elif aktualno_stetje.stevilo_igralcev() == 4:
        <tr> Tu je pomoč za igro v štirih.</tr>

    % else:
        <tr> Tarok se igra v dveh, treh, ali štirih</ tr>
    % end

<p><a href="/stetja/{{id_aktualnega_stetja}}/">Nazaj na štetje.</a></p>