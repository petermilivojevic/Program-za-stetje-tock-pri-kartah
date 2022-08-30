<nav class="level">
    <div class="level-left">
        <div class="buttons has-addons field is-horizontal">
            % for id_stetja, stetje in enumerate(stetja):
            % if stetje == aktualno_stetje:
            <a class="button is-primary is-selected" name="id_stetja" value="{{id_stetja}}">
                {{stetje.ime}}
                <span class="tag is-rounded">{{stetje.igralci}}</span>
            </a>
            % else:
            <a href="/stetja/{{id_stetja}}/" class="button" name="id_stetja" value="{{id_stetja}}">
                {{stetje.ime}}
                <span class="tag is-rounded">{{stetje.igralci}}</span>
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

<table class="table is-hoverable is-fullwidth">
    <thead>
        <tr>
            <form method="POST" action="/stetja/{{id_stetja}}/">
                <td></td>
                <td>
                    <div class="control has-icons-left">
                        <input class="input is-small" type="text" name="ime igralca" placeholder="ime igralca">
                        <span class="icon is-small is-left">
                            <i class="far fa-clipboard-check"></i>
                        </span>
                    </div>
                </td>
                <td>
                    <div class="control has-icons-left">
                        <input class="input is-small" type="text" name="tocke" placeholder="tocke">
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
</table>

% else:

<p>Nimate še nobenega stetja. <a href="/dodaj_stetje/">Dodajte ga!</a></p>