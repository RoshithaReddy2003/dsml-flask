from flask import Flask
import pickle

app = Flask(__name__)

print(__name__)

with open('classifier.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/')
def ping():
    return ({'message': 'ping model application!!'})


if __name__ == "__main__":
    app.run()


def sum_something(a, b):
    return a + b    


def sub_something(a, b):
    return a - b    


def mul_something(a, b):
    return a * b    