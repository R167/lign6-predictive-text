import predict
from collections import Counter

from http.server import HTTPServer, BaseHTTPRequestHandler
import socketserver
from io import BytesIO
import json

PORT = 8080
predictor = None

def initPredictor():
    global predictor
    max_gram = 3

    tokenizer = predict.Tokenizer()
    tokens = []
    tokens = tokens + tokenizer.tokenize_file("data/bee_movie.txt")
    tokens = tokens + tokenizer.tokenize_file("data/moby_dick.txt")

    predictor = predict.Predictor(tokens, tokenizer, max_gram)

class PredictiveTextHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin','*')
        self.end_headers()

        input_str = json.loads(body.decode('utf-8'))["request"]
        predicted = predictor.get_prediction(input_str)

        response = BytesIO()
        response.write(json.dumps(predicted.most_common(10)).encode('utf-8'))
        self.wfile.write(response.getvalue())

def main():


    while True:
        user_input = input("~> ")

        if user_input == ":q":
            return

        predicted = predictor.get_prediction(user_input)
        print(predicted.most_common(10))


if __name__ == "__main__":

    initPredictor()
    print(predictor.get_prediction("You like "))

    PORT = 8080
    Handler = PredictiveTextHandler
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print("serving at port", PORT)
        httpd.serve_forever()
