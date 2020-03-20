
import predict

def main():
    t = predict.Tokenizer("data/short_entry.txt")
    p = predict.Parser(n=2)

    ngrams = p.parse(t.sentences)
    print(ngrams)

if __name__ == "__main__":
    main()

