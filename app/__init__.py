from flask import Flask

app = Flask(__name__)
app.config.from_object("config")

from app.flask_govdelivery.controllers import flask_govdelivery

app.register_blueprint(flask_govdelivery)