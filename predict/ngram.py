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
        self.ngram_size = n - 1
        self.ngrams = {}
        self.tokenizer = Tokenizer()


    def parse(self, sentences):
        s = sentences
        for i in range(len(s) - self.ngram_size):
            # convert the list of grams into a string
            sequence = " ".join(s[i:i+self.ngram_size]) # <<<<< i:i+0 is length 0
            if sequence not in self.ngrams.keys():
                self.ngrams[sequence] = Counter()
            self.ngrams[sequence].update([s[i+self.ngram_size]])

        return self.ngrams

    def predict(self, sentence):
        if len(self.ngrams.keys()) == 0:
            print("Need to parse a file first!")
            return []

        input_tokens = self.tokenizer.tokenize_string(sentence)

        """
        if len(input_tokens) < self.ngram_size:
            print(f"N-Gram size is currently {self.ngram_size}, only {len(input_tokens)} gram found.")
            return []
        """

        input_ngram = " ".join(input_tokens[-self.ngram_size:]).lower()

        if input_ngram in self.ngrams.keys():
            return self.ngrams[input_ngram]
        return []
