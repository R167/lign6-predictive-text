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

  def tokenize_file(self, filename):
    tokens = []
    with open(filename, 'r') as f:
      contents = f.read()
      tokens = self.tokenize_string(contents)
    return tokens


  def tokenize_string(self, contents):
    tokens = []

    contents = self.clean(contents)

    # for sent in nltk.sent_tokenize(contents):
    #   sentences.append(nltk.word_tokenize(sent))
    tokens = nltk.word_tokenize(contents)

    return tokens

  def clean(self, contents):
    return re.sub(r'[^A-Za-z\-]', ' ', contents).lower()
    # return self.cleanup_smart_quotes(contents)
    # jk using regular expressions

  def cleanup_smart_quotes(self, contents):
    targets = []
    replace = []
    for key in REPLACEMENTS:
      contents = contents.replace(key, REPLACEMENTS[key])

    return contents
