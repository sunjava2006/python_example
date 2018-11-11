import flask


app = flask.Flask()

@app.route('/')
def index():
    return 'hello'
