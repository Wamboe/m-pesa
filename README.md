Introduction
This package seeks to help python developers implement the various Mpesa APIs without much hustle. It is based on the REST API whose documentation is available on http://developer.safaricom.co.ke.


Installation using pip
pip install ./dist/mpesa-0.0.1.tar.gz //or whichever version is the latest


Configuration
After downloading the mpesa package, you should fill in your consumer key and consumer and consumer secret and generate a token
then copy and paste this result you get from this function to the other functions.


Usage
As a developer fill in the details that are constant in all the functions and expose the ones that need inut from the client. This should be in line with the details given in the documentation https://developer.safaricom.co.ke/docs

if on production please make sure that you have changed the URL from sandbox to api e.g
for B2C the url is https://sandbox.safaricom.co.ke/mpesa/b2c/v1/paymentrequest. In production it will be https://api.safaricom.co.ke/mpesa/b2c/v1/paymentrequest