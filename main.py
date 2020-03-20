import predict
from collections import Counter


def main():
    p = predict.NGram(n=2)

    tokenizer = predict.Tokenizer()
    p.parse(tokenizer.tokenize_file("data/bee_movie.txt"))
    p.parse(tokenizer.tokenize_file("data/moby_dick.txt"))

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

