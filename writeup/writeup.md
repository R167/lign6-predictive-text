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

We used Python 3.7 with NLTK for the N-Grams. All the n-gram models are stored
using pure python dicts and arrays. To allow dynamic input, we built a basic
webapp using http.server and jQuery. The frontend makes simple POST requests to
the backend which replies with a JSON list of possible completions based on the
input string.

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

Our predictions try matching the longest possible n-grams, up to 5-grams. If
there are no matches, it falls back to 4-grams, all the way to 1-grams. This
lets the autocomplete find the best possible match while being able to adapt if
those fail.

We also added (n-1)-grams, which are used if the user's string does not end in a
space. In a phone keyboard, this would mean they could still be typing the rest
of a word, and we would want to provide autocomplete suggestions for the next
few letters. For this, we take last few complete grams that have been entered
and find the list of n-grams that match those. Then we find all the next words
that _begin_ with start of the word that has been entered. This gives
auto-complete suggestions as you would expect from a phone keyboard.

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

It works surprisingly well! It provides the next word exactly as you would
expect from and n-gram based model. We can definitely see how the source
corporoa influence the output, since a lot of the suggestions mention characters
from the Iliad or boats hunting white whales.

Since we preprocess everything, it runs as fast as you can type. This is
necessary for an autocomplete system since it needs to save time over typing the
rest of the word.

The tool currently just runs a minimal UI through a very basic web interface
which then makes simple requests for the current suggestions. In a production
environment, this is certainly less than ideal and serializing the model to run
on the front end would likely be desirable, but in a local environment, request
lag is less than even the fastest user can type each new character.

## Where the tool consistently failed

The tool we built seemed to have issues in particular with punctuation. This is
mostly because we decided to focus on the words instead of punctuation, since
that's what other autocomplete systems seem to do. To change this we would have
to restructure our tokenization steps, which is where we're stripping the
punctuation.

## Specific ideas on how the tool could be improved

We can always give this a larger corpus. We're using language that doesn't
likely reflect modern conversation. This is one of the downsides of n-grams,
they are very domain specific. In addition, we could hand code in better
handling of punctuation markers/classes to better handle these symbols. To
really start getting at markers like parentheses, quotes, etc. though, we'd
probably need to start building a more advanced model that takes care of the
recursion/paren matching. One other idea is to increase the length that we
consider n-grams for to try and better capture this data, but that still doesn't
really generalize. To really start making things better, we likely need to
implement a fully more powerful model like a Hidden Markov Model.

Further, while we wanted to have the system be able to adjust its weights by
novel user input, we did not have the time/resources to implement it. In the
future, it would be good to let the system use the user's input to improve its
own predictions specific to that user.

## How these advantages and disadvantages would affect implementation in a larger project

If we were deploying this to an actual system, we could use the inputs to
further refine the model. This would be very easy, all we'd need to do is
tokenize the string and call `predictor.parse` to add the new n-grams. As people
keep using the system, it would continuiously refine itself to more accurately
model the users's language. Most phone keyboards already do this, so it's
definitely possible.
