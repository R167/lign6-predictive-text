# N-gram Predictive Text

Predictive text engine for LIGN 6 final project built using n-grams.

## Proposal

Project proposal is visible [here](PROPOSAL.md).

## Results


### Our Task

Our project is an n-gram predictive text engine, similar to what cell phones use for autocomplete.
We wanted to not only implement the basic functionality of "predict the next word," but we also
wanted it to adapt as the user is typing input.

### Tools Used

We used Python with NLTK for the N-Grams. All the n-gram models are stored using pure python dicts
and arrays.
To allow dynamic input, we built a basic webapp using http.server and jquery.

### How We Installed It

We didn't install it, we built it! But to run it yourself run `python server.py` and open `index.html`
in your browser. If you want to try the command line app, run `python main.py`.

### How We Trained Our Model

Our training is done in two stages, tokenization and parsing.

Tokenization is handeled by `tokenizer.py`,
which works in several stages. To start, we strip all smart quotes from the input text. Then this is passed
to NLTK's `word_tokenize()` function, which converts the whole body of text into a series of words.
We then post process the strings by replacing all end of sentence punctuation into an `<eos>` token,
deleting any non-word single tokens, and converting everything to lowercase.

This list of cleaned tokens is then passed to our `NGram` class, which represents a single set of n-grams,
such as bi-grams or tri-grams. Parsing the list of tokens into n-grams is done by sliding a virtual
window over the list of tokens, storing them in a dict where the first `n-1` tokens is the key,
and the last token is stored in a `Counter` object. This way, if we want to find the next word in the
sequence "one two three ____," we only would need to access `ngram['one two three']`.