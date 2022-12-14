% rebase('osnova.tpl')

<h1>Dodajte štetje</h1>
<form method="POST">
    <div class="field">
        <label class="label">Ime</label>
        <div class="control has-icons-left has-icons-right">
            <input class="input" name="ime" type="text" placeholder="ime stetja" value="{{polja.get('ime', '')}}">
        </div>
        % if "ime" in napake:
        <p class="help is-danger">{{ napake["ime"] }}</p>
        % end
    </div>
    <div class="field is-grouped">
        <div class="control">
            <button class="button is-link">Dodaj</button>
        </div>
        <div class="control">
            <a class="button is-link is-light" href="/zacetna_stran/">Prekliči</a>
        </div>
    </div>
</form>
