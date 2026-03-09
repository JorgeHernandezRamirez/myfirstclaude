from flask import Flask


app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Flask app by Jorge - updated again!'

if __name__ == '__main__':
    app.run(debug=True)
