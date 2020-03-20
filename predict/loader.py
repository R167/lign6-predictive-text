import nltk
import re

nltk.download('punkt')

class Tokenizer:
  def __init__(self, filename):
    with open(filename, 'r') as f:
      contents = f.read()
      self.sentences = self.tokenize_sentences(contents)

  def clean(self, contents):
    # get rid of smart quotes
    # sorry about wasting ram
    # contents = contents.replace(u"\u2018", "").replace(u"\u2019", "").replace(u"\u201c","").replace(u"\u201d", "")

    # jk using regular expressions
    return re.sub(r'[^A-Za-z]', ' ', contents)

  def tokenize_sentences(self, contents):
    sentences = []

    contents = self.clean(contents)

    for sent in nltk.sent_tokenize(contents):
      sentences.append(nltk.word_tokenize(sent))

    return sentences
