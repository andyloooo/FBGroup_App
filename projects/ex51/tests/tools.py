from nose.tools import *
import re

def assert_response(resp, contains=None, matches=None, headers=None, status="200"):

	assert status in resp.status, "Expected response %r not in %r" % (status, resp.status)
	
	if status == "200":
		assert resp.data, "Response data is empty." #error message when data is empty
		
	if contains:
		assert contains in resp.data, "Response does not contain %r" % contains # asserts error if contains is in data
	
	if matches:
		reg = re.compile(matches)
		assert reg.matches(resp.data), "Response does not match %r" % matches # assert error if data does not match
	
	if headers:
		assert_equal(resp.headers, headers)