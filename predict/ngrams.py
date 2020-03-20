import nltk
import re

class Parser:
    def __init__(self, n=3):
        self.ngram_size = n
        self.ngrams = {}

    def parse(self, sentences):
        for s in sentences:
            for i in range(len(s) - self.ngram_size):
                # convert the list of grams into a string
                sequence = " ".join(s[i:i+self.ngram_size])
                if sequence not in self.ngrams.keys():
                    self.ngrams[sequence] = []
                self.ngrams[sequence].append(s[i+self.ngram_size])

        return self.ngrams

    def predict(self, sentence):
        if len(self.ngrams.keys()) == 0:
            print("Need to parse a file first!")
            return

        sentence = re.sub(r'[^A-Za-z]', ' ', sentence)
        input_tokens = nltk.word_tokenize(sentence)

        if len(input_tokens) < self.ngram_size:
            print(f"N-Gram size is currently {self.ngram_size}, only {len(input_tokens)} gram found.")
            return []

        input_ngram = " ".join(input_tokens[-self.ngram_size:]).lower()

        if input_ngram in self.ngrams.keys():
            return self.ngrams[input_ngram]
        return []
