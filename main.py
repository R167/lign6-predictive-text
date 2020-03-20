import predict
from collections import Counter


def main():
    p = predict.NGram(n=2)

    bee_movie = predict.Tokenizer()
    p.parse(bee_movie.tokenize_file("data/bee_movie.txt")))
    # moby_dick = predict.Tokenizer("data/moby_dick.txt")

    print(p.ngrams)

    while True:
        user_input = input("~> ")

        if user_input == ":q":
            return

        predicted = p.predict(user_input)
        if not predicted == []:
            #print(" ".join(set(p.predict(user_input))))
            print(p.predict(user_input))


if __name__ == "__main__":
    main()

