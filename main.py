
import predict


def main():
    p = predict.Parser(n=2)

    bee_movie = predict.Tokenizer("data/bee_movie.txt")
    moby_dick = predict.Tokenizer("data/moby_dick.txt")

    p.parse(bee_movie.sentences)
    p.parse(moby_dick.sentences)

    while True:
        user_input = input(": ")

        if user_input == "!quit":
            return

        predicted = p.predict(user_input)
        if predicted == []:
            print("No N-Grams match")
        else:
            print("Predicted words:", " ".join(p.predict(user_input)))

if __name__ == "__main__":
    main()

