import requests
import unittest
try:
    from unittest import mock
except ImportError:
    import mock


class MockResponse:
    def __init__(self, json_data, status_code, headers={}):
        self.json_data = json_data
        self.status_code = status_code
        self.headers = headers

    def json(self):
        return self.json_data


def mocked_requests_get(*args, **kwargs):

    import pdb
    pdb.set_trace()

    if args[0] == 'http://someurl.com/test.json':
        return MockResponse({"key1": "value1"}, 200)
    elif args[0] == 'http://someotherurl.com/anothertest.json':
        return MockResponse({"key2": "value2"}, 200)

    return MockResponse(None, 404)


def mocked_requests_post(*args, **kwargs):

    if '/collection/token/' in args[0]:
        return MockResponse({"access_token": "token"}, 200)
    elif "/collection/v1_0/requesttopay" in args[0]:
        return MockResponse({"key2": "value2"}, 200)

    return MockResponse(None, 404)


def mocked_requests_session(*args, **kwargs):
    if '/collection/token/' in args[1]:
        return MockResponse({"access_token": "token"}, 200)
    elif "/collection/v1_0/requesttopay" in args[1]:
        return MockResponse({"key2": "value2"}, 200)
