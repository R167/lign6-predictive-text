import nltk
import re
from collections import Counter

from . import Tokenizer

# n-gram =
# [`n - 1` previous words] + prediction
#
# so a 1-gram is just a current/valid word prediction
class NGram:
    def __init__(self, n=3, limit=-1):
        self.max_limit = limit
        self.ngram_size = n
        self.ngrams = {}
        self.tokenizer = Tokenizer()


    def parse(self, sentences):
        s = sentences
        for i in range(len(s) - (self.ngram_size - 1)):
            # convert the list of grams into a string
            sequence = " ".join(s[i:i+self.ngram_size-1]) # <<<<< i:i+0 is length 0
            if sequence not in self.ngrams.keys():
                self.ngrams[sequence] = Counter()
            self.ngrams[sequence].update([s[i+self.ngram_size-1]])

        return self.ngrams

    def predict(self, sentence, raw=False):
        if len(self.ngrams.keys()) == 0:
            print("Need to parse a file first!")
            return []

        if sentence == "":
            return self.ngrams[""]

        # print(repr(sentence))
        input_tokens = self.tokenizer.tokenize_string(sentence)

        """
        if len(input_tokens) < self.ngram_size:
            print(f"N-Gram size is currently {self.ngram_size}, only {len(input_tokens)} gram found.")
            return []
        """

        input_ngram = None
        if raw:
            input_ngram = sentence
        else:
            input_ngram = NGram.construct_key(input_tokens[1-self.ngram_size:])

        if input_ngram in self.ngrams.keys():
            return self.ngrams[input_ngram]
        return Counter()

    @staticmethod
    def construct_key(token_list):
        return " ".join(token_list).lower()

class Predictor:
    def __init__(self, tokens, tokenizer, max_gram):
        self.tokenizer = tokenizer
        self.max_gram = max_gram
        self.tokens = tokens
        self.ngrams = {}
        self.init_ngrams()

    def init_ngrams(self):
        for i in range(1, self.max_gram + 1):
            ngram = NGram(n=i)
            ngram.parse(self.tokens)
            self.ngrams[i] = ngram

    # Returns a counter of predictions
    def get_prediction(self, sentence):
        tokens = self.tokenizer.tokenize_string(sentence)
        if tokens[-1] == Tokenizer.EOS:
            tokens.append('')
        elif sentence[-1] == ' ':
            tokens.append('')

        # trim down search length
        search = tokens[-self.max_gram:]

        # if the last char was a space, we don't want to predict any more for this word
        for i in range(len(search), 0, -1):
            ngram = self.ngrams[i]
            prefix = search[-1]

            key = NGram.construct_key(search[-i:-1])
            print(key)
            print(prefix)
            options = ngram.predict(key, raw=True)

            matches = filter(lambda w: w[0].startswith(prefix), options.items())

            output = Counter(dict(matches))
            if len(output) > 0:
                return output

        return Counter()
