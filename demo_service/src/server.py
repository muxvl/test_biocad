from flask import Flask

server = Flask(__name__)

@server.route("/")
def hello():
    return "Hello, this is my DEMO PROJECT for BIOCAD!"

if __name__ == "__main__":
   server.run(host='0.0.0.0', port=32777, debug=True)