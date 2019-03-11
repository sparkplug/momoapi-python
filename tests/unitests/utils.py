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
    if "/requesttopay" in args[0]:
        return MockResponse({
            "amount": 100,
            "currency": "UGX",
            "financialTransactionId": 23503452,
            "externalId": 947354,
            "payer": {
                "partyIdType": "MSISDN",
                "partyId": 4656473839
            },
            "status": "SUCCESSFUL"
        }, 200)

    return MockResponse(None, 404)


def mocked_requests_post(*args, **kwargs):

    if '/collection/token/' in args[0]:
        return MockResponse({"access_token": "token"}, 200)
    elif "/collection/v1_0/requesttopay" in args[0]:
        return MockResponse({"key2": "value2"}, 200)
    elif "apiuser" in args[0] and "apikey" in args[0]:
        return MockResponse({
            "apiKey": "dummykey"
        }, 200)

    return MockResponse(None, 404)


def mocked_requests_session(*args, **kwargs):
    if '/token/' in args[1]:
        return MockResponse({"access_token": "token"}, 200)
    elif '/balance' in args[1]:
        return MockResponse({
            "availableBalance": "500",
            "currency": "UGX"
        }, 200)
    elif "/requesttopay" in args[1] and args[0] == 'POST':
        return MockResponse({}, 200)
    elif "transfer" in args[1] and args[0] == 'POST':
        return MockResponse({}, 200)
    elif ("/requesttopay" in args[1] or "/transfer" in args[1]) and args[0] == 'GET':
        return MockResponse({
            "amount": 100,
            "currency": "UGX",
            "financialTransactionId": 23503452,
            "externalId": 947354,
            "payer": {
                "partyIdType": "MSISDN",
                "partyId": 4656473839
            },
            "status": "SUCCESSFUL"
        }, 200)
    else:
        return MockResponse({}, 200)
