from flask import Blueprint, request, Response

flask_govdelivery = Blueprint("flask-govdelivery", __name__, url_prefix="")


@flask_govdelivery.errorhandler(400)
def missing_parameter(parameter):
    message = "You are missing the {} parameter".format(parameter)
    return Response(message, 400)


@flask_govdelivery.route("/new", methods=['POST'])
def hello():
    if 'test' not in request.form:
        return missing_parameter('test')
    return "works"