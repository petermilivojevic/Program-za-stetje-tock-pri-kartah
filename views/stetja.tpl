<nav class="level">
    <div class="level-left">
        <div class="buttons has-addons field is-horizontal">
            % for id_stetja, stetje in enumerate(stetja):
            <a href="/stetja/{{id_stetja}}/" class="button" name="id_stetja" value="{{id_stetja}}">
                {{stetje.ime}}
                <span class="tag is-rounded">{{stetje.stevilo_igralcev()}}</span>
            </a>
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
