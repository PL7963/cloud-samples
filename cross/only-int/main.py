import os

from flask import Flask, request

app = Flask(__name__)
onlyint = os.getenv("ONLY_INT", True)

@app.route('/', methods=['POST'])
def process(): # keep int only
    data = request.get_json().get('content', '')
    result = ''
    if not onlyint:
        return data
    else:
        for i in range(len(data)):
            if data[i].isdigit():
                result += data[i]
    return result

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
