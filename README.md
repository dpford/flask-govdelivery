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

Depends on the govdelivery python wrapper being installed:
https://github.com/rosskarchner/govdelivery