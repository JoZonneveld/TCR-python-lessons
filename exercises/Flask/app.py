from flask import Flask
from Controller.ControllerConfig import controllers

app = Flask(__name__)

for controller in controllers:
    app.register_blueprint(controller)


@app.route('/')
def hello_world():
    return 'App!'


if __name__ == '__main__':
    app.run()
