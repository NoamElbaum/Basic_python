from flask import Flask

app = Flask('__name__')


@app.route('/')
def home():
    return "0"


@app.route('/1')
def a():
    return "1"


@app.route('/2')
def b():
    return "2"


@app.route('/3')
def c():
    return "3"


if __name__ == '__main__':
    app.run(debug=True)
