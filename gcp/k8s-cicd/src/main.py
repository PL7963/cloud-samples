import flask

app = flask.Flask(__name__)

@app.route('/')
def index():
    return 'i am a cute cat'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)