<nav class="level">
    <div class="level-left">
        <div class="buttons has-addons field is-horizontal">
            % for id_stetja, stetje in enumerate(stetja):
            % if stetje == aktualno_stetje:
            <a class="button is-primary is-selected" name="id_stetja" value="{{id_stetja}}">
                {{stetje.ime}}
                <span class="tag is-rounded">{{stetje.stevilo_igralcev()}}</span>
            </a>
            % else:
            <a href="/stetja/{{id_stetja}}/" class="button" name="id_stetja" value="{{id_stetja}}">
                {{stetje.ime}}
                <span class="tag is-rounded">{{stetje.stevilo_igralcev()}}</span>
            </a>
            % end
            % end
        </div>

    </div>

    <div class="level-right">
            <div class="level-item">
                <a class="button is-info" href="/dodaj_stetje/">dodaj stetje</a>
            </div>
        </form>
    </div>
</nav>

% if aktualno_stetje:

<thead>
    <tr>
        <form method="POST" action="/stetja/{{id_aktualnega_stetja}}/">
            <td></td>
            <td>
                <div class="control has-icons-left">
                    <input class="input is-small" type="text" name="ime" placeholder="ime igralca" value="{{polja.get('ime', '')}}">
                    <span class="icon is-small is-left">
                        <i class="far fa-clipboard-check"></i>
                    </span>
                </div>
                % if "ime" in napake:
                <p class="help is-danger">{{ napake["ime"] }}</p>
                % end
            </td>
            <td>
                <div class="control has-icons-left">
                    <input class="input is-small" type="number" step="1" name="tocke" placeholder="0">
                    <span class="icon is-small is-left">
                        <i class="far fa-calendar-alt"></i>
                    </span>
                </div>
            </td>
            <td>
                <div class="control">
                    <button class="button is-info is-small">dodaj</button>
                </div>
            </td>
        </form>
    </tr>
</thead>
<tbody>
    % for id_igralca, igralec in enumerate(aktualno_stetje.igralci):
    <tr>
        <td>{{ igralec.ime }}: {{ igralec.vsota_tock() }} točk</td>
        <form method="POST" action="/stetja/{{id_aktualnega_stetja}}/{{id_igralca}}/">
            <td></td>
            
            <td>
                <input class="input is-small" type="number" step="1" name="nove_tocke" placeholder="dodaj točke">
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


<p><a href="/stetja/{{id_aktualnega_stetja}}/pomoc_tarok/">Pomoč pri štetju za tarok</a></p>
<p><a href="/stetja/{{id_aktualnega_stetja}}/pomoc_enka/">Pomoč pri štetju za enko</a></p>

% else:

<p>Nimate še nobenega stetja. <a href="/dodaj_stetje/">Dodajte ga!</a></p>
% end