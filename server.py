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
    max_gram = 5

    tokenizer = predict.Tokenizer()
    tokens = []
    tokens = tokens + tokenizer.tokenize_file("data/bee_movie.txt")
    tokens = tokens + tokenizer.tokenize_file("data/moby_dick.txt")
    tokens = tokens + tokenizer.tokenize_file("data/the_iliad.txt")

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


if __name__ == "__main__":

    initPredictor()

    PORT = 8080
    Handler = PredictiveTextHandler
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print("serving at port", PORT)
        httpd.serve_forever()
