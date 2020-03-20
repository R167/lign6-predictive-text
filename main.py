import predict
from collections import Counter


def main():
    p = predict.NGram(n=4)

    tokenizer = predict.Tokenizer()
    tokens = []
    tokens = tokens + tokenizer.tokenize_file("data/bee_movie.txt")
    tokens = tokens + tokenizer.tokenize_file("data/moby_dick.txt")

    p.parse(tokens)

    while True:
        user_input = input("~> ")

        if user_input == ":q":
            return

        predicted = p.predict(user_input)
        if not predicted == []:
            #print(" ".join(set(p.predict(user_input))))
            print(p.predict(user_input).most_common(3))


if __name__ == "__main__":
    main()

