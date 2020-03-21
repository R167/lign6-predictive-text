---
geometry: margin=1in
---

# Predictive text engine

Written by Winston Durand and Thomas Lauer

This entire source of this project is available at [github.com/R167/lign6-predictive-text](https://github.com/R167/lign6-predictive-text)

## Our task

Our project is an n-gram predictive text engine, similar to what cell phones use
for autocomplete. We wanted to not only implement the basic functionality of
"predict the next word," but we also wanted it to adapt as the user is typing
input.

## What toolkit we used (e.g. versions, languages)

We used Python with NLTK for the N-Grams. All the n-gram models are stored using
pure python dicts and arrays. To allow dynamic input, we built a basic webapp
using http.server and jquery.

## How you installed it

We didn't install it, we built it! But to run it yourself run `python server.py`
and open `index.html` in your browser. If you want to try the command line app,
run `python main.py`. The code dependencies are managed using pipenv.

## The corpus or data you used

For our model, we primarily used openly available works from project Gutenberg
(e.g. The Iliad and Moby Dick). Thomas inisted on using a freely available
version of The Bee Movie script "for the memes" as well. We assumed our data was
mosly devoid of formatting data (read: plaintext) and that it was generally well
behaved without word breaks across lines, etc. We did take certain measures to
clean it up, such as removing "smart quotes" and various minor formatting like
surrounding underscores to delineate italics.

The model also makes some pretty large assumptions about punctuation, namely
that most of it doesn't matter (we weren't getting any useful data from commas,
quotes, etc.), and also that all ending punctuation can be encoded similarly
(just as an "end of sentence" marker).

## How you trained the model (or, what the pre-trained model was trained on)

Our training is done in two stages, tokenization and parsing.

Tokenization is handeled by `tokenizer.py`, which works in several stages. To
start, we strip all smart quotes from the input text. Then this is passed to
NLTK's `word_tokenize()` function, which converts the whole body of text into a
series of words. We then post process the strings by replacing all end of
sentence punctuation into an `<eos>` token, deleting any non-word single tokens,
and converting everything to lowercase.

This list of cleaned tokens is then passed to our `NGram` class, which
represents a single set of n-grams, such as bi-grams or tri-grams. Parsing the
list of tokens into n-grams is done by sliding a virtual window over the list of
tokens, storing them in a dict where the first `n-1` tokens is the key, and the
last token is stored in a `Counter` object. This way, if we want to find the
next word in the sequence "one two three ____," we only would need to access
`ngram['one two three']`.

## The code used to run the tool (Comment your code, and provide the source)

### `predict/__init__.py`: just boiler plate

```{.python include=predict/__init__.py}
```

### `predict/ngram.py`: takes care of building the ngrams and parser

```{.python include=predict/ngram.py}
```

### `predict/tokenizer.py`: tokenizer for processing input

```{.python include=predict/tokenizer.py}
```

### `ui/index.html`: barebones ui for feedback as you type

```{.html include=index.html}
```

### `server.py`: super barebones server to handle backend

```{.python include=server.py}
```

## What the tool consistently "got right"

## Where the tool consistently failed

The tool we built seemed to have issues in particular with punctuation.

## Specific ideas on how the tool could be improved

## How these advantages and disadvantages would affect implementation in a larger project.
