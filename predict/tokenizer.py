import nltk
import re

nltk.download('punkt')

REPLACEMENTS = {
  u"\u2018": "", # Start smart quotes
  u"\u2019": "",
  u"\u201c": '',
  u"\u201d": '',
  u"\u2014": ' - ', # Em dashes
}

REJECTS = ['-']

class Tokenizer:

  EOS = "<eos>"

  EOS_EQUIVALENT = r'^[\.!?]$'
  SINGLE_CHAR = r'^[\W_-]$'

  def tokenize_file(self, filename):
    tokens = []
    with open(filename, 'r') as f:
      contents = f.read()
      tokens = self.tokenize_string(contents)
    return tokens


  def tokenize_string(self, contents):
    tokens = []

    # contents = self.clean(contents)

    # for sent in nltk.sent_tokenize(contents):
    #   sentences.append(nltk.word_tokenize(sent))
    contents = self.pre_cleanup(contents)
    tokens = nltk.word_tokenize(contents)
    tokens = self.post_cleanup(tokens)

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

  # Clean up any invalid characters
  def pre_cleanup(self, contents):
    cont = self.cleanup_smart_quotes(contents)
    return cont

  # Reject any tokens we don't care about or canonicalize them
  def post_cleanup(self, tokens):
    # Steps:

    # - make everything lowercase
    tokens = [token.lower() for token in tokens]

    # - Prepend "<EOS>"
    output_tokens = [self.EOS]

    # - Canonicalize all [\.!?] etc. to a "<EOS>"
    for token in tokens:
      output_tokens.append(re.sub(self.EOS_EQUIVALENT, self.EOS, token))

    # - Delete any other single character \W
    output_tokens = [token for token in output_tokens if not re.match(self.SINGLE_CHAR, token)]


    # - Delete leading/trailing [_]

    return output_tokens
