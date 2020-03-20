

class Parser:
    def __init__(self, n=3):
        self.ngram_size = n
        self.ngrams = {}

    def parse(self, sentences):
        for s in sentences:
            for i in range(len(s) - self.ngram_size - 1):
                # convert the list of grams into a string
                sequence = " ".join(s[i:i+self.ngram_size])
                if sequence not in self.ngrams.keys():
                    self.ngrams[sequence] = []
                self.ngrams[sequence].append(s[i+self.ngram_size+1])

        return self.ngrams
