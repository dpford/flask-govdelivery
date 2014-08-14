from flask import Flask

app = Flask(__name__)
app.config.from_object("config")

from flask_govdelivery.govdelivery.controllers import govdelivery

app.register_blueprint(govdelivery)