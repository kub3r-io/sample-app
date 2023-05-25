from cto_ai import ux, prompt, sdk
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    message1 = "Hello, World!"
    message2 = "n\I'm in a service running now!"
    return message1+message2

if __name__ == '__main__':
    ux.print("Starting server")
    app.run(host='0.0.0.0', port=8080)

