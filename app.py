from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return '<h1>Hello World :)</h1>'


if __name__ == '__main__':
    app.run()


@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=""):
    return f"Hello {name}"


@app.route('/temperature/')
@app.route('/temperature/<number>')
def temperature(number):
    return str((float(number) * 9/5) + 32)