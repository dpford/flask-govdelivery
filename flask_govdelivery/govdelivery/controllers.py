import os
from flask import Blueprint, request, Response, redirect, jsonify
from govdelivery.api import GovDelivery

ACCOUNT_CODE = os.environ.get('GOVDELIVERY_ACCOUNT_CODE')
SUBSCRIPTION_SUCCESS_URL = os.environ.get('SUBSCRIPTION_SUCCESS_URL', '/')
SUBSCRIPTION_USER_ERROR_URL = os.environ.get('SUBSCRIPTION_USER_ERROR_URL', '/')
SUBSCRIPTION_SERVER_ERROR_URL = os.environ.get('SUBSCRIPTION_SERVER_ERROR_URL', '/')
gd = GovDelivery(account_code=ACCOUNT_CODE)
RESULT_PASSING = {'result': 'pass'}
RESULT_FAILING = {'result': 'fail'}
REQUIRED_PARAMS = ['email', 'code']

govdelivery = Blueprint("flask-govdelivery", __name__, url_prefix="")


def missing_parameter(parameter):
    message = 'You are missing the "{}" parameter'.format(parameter)
    return Response(message, 400)


def fail_with_code_and_message(message, code=500):
    return Response(message, code)


def extract_answers_from_request(request):
    answers = [(param.split('_')[1], value) for param, value in
               request.form.items() if param.startswith('questionid')]
    return answers


@govdelivery.route("/subscriptions/new/", methods=['POST'])
def new():
    """
    Function that checks to see if the request is AJAX, attempts to subscribe
    the user, then either redirects to an error/success page (non-AJAX) or
    in the case of AJAX, returns some JSON to tell the front-end.
    """
    is_ajax = request.is_xhr
    if is_ajax:
        passing_response = jsonify(RESULT_PASSING)
        failing_response = jsonify(RESULT_FAILING)
    else:
        passing_response = redirect(SUBSCRIPTION_SUCCESS_URL)
        failing_response = redirect(SUBSCRIPTION_SERVER_ERROR_URL)
    for required_param in REQUIRED_PARAMS:
        if required_param not in request.form or not request.form[required_param]:
            return jsonify(RESULT_FAILING) if is_ajax else \
                redirect(SUBSCRIPTION_USER_ERROR_URL)
    email_address = request.form['email']
    codes = request.form.getlist('code')
    try:
        subscription_response = gd.set_subscriber_topics(email_address, codes)
        if subscription_response.status_code != 200:
            return failing_response
    except Exception:
        return failing_response
    answers = extract_answers_from_request(request)
    for question_id, answer_text in answers:
        response = gd.set_subscriber_answers_to_question(email_address,
                                                         question_id,
                                                         answer_text)
    return passing_response


@govdelivery.route("/form-test/", methods=['GET'])
def form_test():
    return Response("Worked!")
