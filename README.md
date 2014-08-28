flask-govdelivery
=================

A flask wrapper for the govdelivery API

It currently provides a form handler that allows for subscription to an arbitrary number of topics. Forms that submit to it should look roughly like this:

```html
<form action="/subscriptions/new" method="POST" enctype="application/x-www-form-urlencoded">

<input type="hidden" name="code" value="SOME_TOPIC_CODE">
<input type="hidden" name="code" value="ANOTHER_TOPIC_CODE">
<input type="input" name="questionid_12345"/>
<input type="email" name="email" >
<button>Sign up</button>
</form>
```
The following environment variables need to be set:

* GOVDELIVERY_BASE_URL
* GOVDELIVERY_ACCOUNT_CODE
* GOVDELIVERY_USER
* GOVDELIVERY_PASSWORD
* SUBSCRIPTION_SUCCESS_URL
* SUBSCRIPTION_USER_ERROR_URL
* SUBSCRIPTION_SERVER_ERROR_URL

(URLs can be relative)

The text inside any form input with a name starting with "questionid_" will be included in the subscription request.

Depends on the govdelivery python wrapper being installed:
https://github.com/rosskarchner/govdelivery