from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "Hello World! This is A app YAY!!! CLOUDNATIVE ROADSHOW MOSCOW!!!"

if __name__ == "__main__":
    application.run()
