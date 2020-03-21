---
geometry: margin=1in
---

# Predictive text engine

Written by Winston Durand and Thomas Lauer

## Our task

## What toolkit we used (e.g. versions, languages)

## How you installed it

## The corpus or data you used

## How you trained the model (or, what the pre-trained model was trained on)

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
