import nltk

nltk.download('punkt')

class Tokenizer:
  def __init__(self, filename):
    with open(filename, 'r') as f:
      contents = f.read()
      self.sentences = self.tokenize_sentences(contents)

  def tokenize_sentences(self, contents):
    sentences = []
    # get rid of smart quotes
    # sorry about wasting ram
    contents = contents.replace(u"\u2018", "").replace(u"\u2019", "").replace(u"\u201c","").replace(u"\u201d", "")
    for sent in nltk.sent_tokenize(contents):
      sentences.append(nltk.word_tokenize(sent))

    return sentences
