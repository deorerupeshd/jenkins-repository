from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
        return 'Hello, world! This is a Flask web application, hi jenkins.'

if __name__ == '__main__':
        app.run(debug=False, host='0.0.0.0', port=5000)
