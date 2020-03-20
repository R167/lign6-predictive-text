import nltk
import re

nltk.download('punkt')

REPLACEMENTS = {
  u"\u2018": "'", # Start smart quotes
  u"\u2019": "'",
  u"\u201c": '"',
  u"\u201d": '"',
  u"\u2014": ' - ', # Em dashes
}

class Tokenizer:
  def __init__(self, filename):
    with open(filename, 'r') as f:
      contents = f.read()
      self.sentences = self.tokenize_sentences(contents)

  def clean(self, contents):
    return self.cleanup_smart_quotes(contents)
    # jk using regular expressions
    # return re.sub(r'[^A-Za-z]', ' ', contents).lower()

  def tokenize_sentences(self, contents):
    sentences = []

    contents = self.clean(contents)

    # for sent in nltk.sent_tokenize(contents):
    #   sentences.append(nltk.word_tokenize(sent))
    sentences = nltk.word_tokenize(contents)

    return sentences

  def cleanup_smart_quotes(self, contents):
    targets = []
    replace = []
    for key in REPLACEMENTS:
      contents = contents.replace(key, REPLACEMENTS[key])

    return contents
