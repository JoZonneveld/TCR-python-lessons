from flask import Flask
from Flask.Controller.ControllerConfig import controllers
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

for controller in controllers:
    app.register_blueprint(controller)


@app.route('/')
def hello_world():
    return 'App!'


if __name__ == '__main__':
    app.run()
