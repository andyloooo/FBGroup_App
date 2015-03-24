from nose.tools import *
from bin.app import app
from tests.tools import assert_response

def test_index():
	# check that we get a 404 on the / URL
	resp = app.request("/") 
	# app.request(localpart='/', method='GET', data=None, host='0.0.0.0:8080',
       #     headers=None, https=False)
	assert_response(resp, status="404")
	# assert_response(resp, contains=None, matches=None, headers=None, status="200")
	
	
	# test our first GET request to /hello
	resp = app.request("/hello")
	assert_response(resp)
	
	# make sure default values work for the format
	resp = app.request("/hello", method = "POST")
	assert_response(resp, contains ="Nobody")
	
	# test that we get expected values
	data = {'name': 'Zed', 'greet': 'Hola'}
	resp = app.request("/hello", method="POST", data=data)
	assert_response(resp, contains = "Zed") # contains makes sure there are certain values in the response