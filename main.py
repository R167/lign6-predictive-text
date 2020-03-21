import predict
from collections import Counter
import json


def main():

    max_gram = 3

    tokenizer = predict.Tokenizer()
    tokens = []
    tokens = tokens + tokenizer.tokenize_file("data/bee_movie.txt")
    tokens = tokens + tokenizer.tokenize_file("data/moby_dick.txt")

    predictor = predict.Predictor(tokens, tokenizer, max_gram)

    while True:
        user_input = input("~> ")

        if user_input == ":q":
            return

        predicted = predictor.get_prediction(user_input)
        print(json.dumps(predicted.most_common(10)))
        # print(predicted)


if __name__ == "__main__":
    main()

