
import predict


def main():
    t = predict.Tokenizer("data/bee_movie.txt")
    p = predict.Parser(n=2)

    p.parse(t.sentences)

    while True:
        user_input = input(": ")

        if user_input == "!quit":
            return

        print(p.predict(user_input))

if __name__ == "__main__":
    main()

