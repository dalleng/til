document.addEventListener('DOMContentLoaded', function() {
    const search = document.getElementById('search');
    const searchData = document.getElementById('searchIndex');

    if (search && searchData) {
        const { index, terms } = JSON.parse(searchData.textContent);
        const vocabulary = Object.entries(terms);
        const items = document.querySelectorAll('.notes li[data-category]');
        const tags = document.querySelectorAll('.filters button.tag');
        const status = document.getElementById('search-status');
        let category = 'all';

        function filterNotes() {
            /*
             * Split the search text into words, treating punctuation and whitespace as separators:
             *
             * - \p{L} — any Unicode letter, including accented letters.
             * - \p{N} — any Unicode number.
             * - _ — underscores are included in words.
             * - [...]+ — matches one or more of those characters.
             * - g — finds every match.
             * - u — enables Unicode matching, required for \p{…}.
             *
             * For example, applying this to "Python, café foo_bar".toLowerCase() produces:
             * ["python", "café", "foo_bar"]
             *
             * .match() returns null if nothing matches, so || [] provides an empty array.
             */
            const query = search.value.toLowerCase().match(/[\p{L}\p{N}_]+/gu) || [];
            const matches = new Set();
            const matchingStems = new Set();
            for (const term of query) {
                // Resolve words seen in the notes to their build-time Snowball stems.
                const stem = Object.hasOwn(terms, term) ? terms[term] : term;
                if (Object.hasOwn(index, stem)) {
                    matchingStems.add(stem);
                }
                // Find prefixes of at least three characters in the original words,
                // then combine their stem groups with the whole-word matches.
                if ([...term].length >= 3) {
                    for (const [word, wordStem] of vocabulary) {
                        if (word.startsWith(term)) matchingStems.add(wordStem);
                    }
                }
            }
            for (const stem of matchingStems) {
                index[stem].forEach(id => matches.add(id));
            }

            let count = 0;
            items.forEach(item => {
                const matchesCategory = category === 'all' || item.dataset.category === category;
                const matchesSearch = query.length === 0 || matches.has(item.id);
                item.hidden = !(matchesCategory && matchesSearch);
                if (!item.hidden) count++;
            });
            status.textContent = count === 0 ? 'No notes match your search.'
                : `${count} ${count === 1 ? 'note' : 'notes'}`;
        }

        search.addEventListener('input', filterNotes);
        tags.forEach(tag => {
            tag.addEventListener('click', function() {
                category = this.textContent.trim();
                tags.forEach(t => {
                    const active = t === this;
                    t.classList.toggle('active', active);
                    t.setAttribute('aria-pressed', String(active));
                });
                filterNotes();
            });
        });
        filterNotes();
    }

    document.addEventListener('keypress', (event) => {
        if (event.key !== '.') {
            return;
        }
        const baseURL = 'https://github.dev/dalleng/til';
        let goToURL = baseURL;
        const category = document.querySelector("meta[name='category']")?.content;
        if (category) {
            const htmlPath = window.location.pathname.split('/').at(-1);
            const title = htmlPath.replace(/\.html$/, '');
            goToURL = `${baseURL}/blob/main/${category}/${title}.md`;
        }
        window.location = goToURL;
    });
});
