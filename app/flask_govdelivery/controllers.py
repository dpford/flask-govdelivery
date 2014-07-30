import os
from flask import Blueprint, request, Response, render_template
from govdelivery.api import GovDelivery

ACCOUNT_CODE = os.environ.get('GOVDELIVERY_ACCOUNT_CODE')
gd = GovDelivery(account_code=ACCOUNT_CODE)

flask_govdelivery = Blueprint("flask-govdelivery", __name__, url_prefix="")


def missing_parameter(parameter):
    message = 'You are missing the "{}" parameter'.format(parameter)
    return Response(message, 400)

def fail_with_code_and_message(message, code=500):
    return Response(message, code)

def extract_answers_from_request(request):
    answers = [(param.split('_')[1], value) for param, value in \
               request.form.items() if param.startswith('questionid')]
    return answers


@flask_govdelivery.route("/new", methods=['POST'])
def new():
    for required_param in ['email','code']:
            if required_param not in request.form:
                return missing_parameter(required_param)
    email_address = request.form['email']
    codes = request.form.getlist('code')
    try:
        subscription_response = gd.set_subscriber_topics(email_address, codes)
        if subscription_response.status_code != 200:
            return fail_with_code_and_message(500, "subscription attempt failed")
    except Exception, e:
        return fail_with_code_and_message(500, "subscription attempt failed")
    answers = extract_answers_from_request(request)
    for question_id, answer_text in answers:
            response = gd.set_subscriber_answers_to_question(email_address, question_id, answer_text)
    return Response("subscription successful!")