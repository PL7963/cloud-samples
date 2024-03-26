import time
from flask import Flask

app = Flask('__name__')

@app.route('/')
def main():
    time.sleep(10)
    return "This take a long time to proccess uwu"


if __name__ == '__main__':
    app.run(host='0.0.0.0',port='8080')
