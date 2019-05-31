import flask
from flask import render_template

app = flask.Flask(__name__)

@app.route('/')
def index():
    values = {"val1": 100, "val2" :200}
    return render_template('index.html', values=values)

if __name__ == '__main__':
    app.run(debug=True)

