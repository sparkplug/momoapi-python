"""
Base implementation of the MTN API client

@author: Moses Mugisha
"""


import json
import uuid
try:
    from json.decoder import JSONDecodeError
except ImportError:
    JSONDecodeError = ValueError

import requests
from requests import Request, Session
from requests._internal_utils import to_native_string
from requests.auth import AuthBase
from requests.auth import HTTPBasicAuth


from .errors import APIError
from .utils import requests_retry_session


class Response:

    def __init__(self, body, code, headers):
        self.body = body
        self.code = code
        self.headers = headers
        self.data = body


class MoMoAuth(AuthBase):
    """Attaches Authentication to the given Request object."""

    def __init__(self, token):

        self.token = token

    def __call__(self, r):
        # modify and return the request

        r.headers['Authorization'] = "Bearer " + to_native_string(self.token)
        return r


class MomoApi(object):

    def __init__(
            self,
            auth_key,
            user_id,
            api_secret,
            base_url="https://ericssonbasicapi2.azure-api.net",
            ** kwargs):
        super(MomoApi, self).__init__(**kwargs)
        self._session = Session()
        self.api_secret = api_secret
        self.user_id = user_id
        self.auth_key = auth_key
        self.base_url = base_url

    def request(self, method, url, headers, post_data=None):
        self.authToken = self.getAuthToken().json()["access_token"]
        request = Request(
            method,
            url,
            data=json.dumps(post_data),
            headers=headers,
            auth=MoMoAuth(self.authToken))

        prepped = self._session.prepare_request(request)

        resp = requests_retry_session(sesssion=self._session).send(prepped,
                                                                   verify=False
                                                                   )
        return self.interpret_response(resp)

    def interpret_response(self, resp):
        rcode = resp.status_code
        rheaders = resp.headers

        try:
            rbody = resp.json()
        except JSONDecodeError:
            rbody = resp.text
            resp = Response(rbody, rcode, rheaders)

        if not (200 <= rcode < 300):
            self.handle_error_response(rbody, rcode, resp.text, rheaders)

        return resp

    def handle_error_response(self, rbody, rcode, resp, rheaders):

        raise APIError(
            "Invalid response object from API: {0} (HTTP response code "
            "was {1})".format(rbody, rcode),
            rbody, rcode, resp)

    def request_headers(self, api_key, method):
        headers = {}

        return headers

    def getAuthToken(self):
        data = json.dumps({})
        headers = {
            "Content-Type": "application/json",
            "Ocp-Apim-Subscription-Key": self.auth_key
        }
        response = requests.post(

            "{0}/collection/token/".format(self.base_url),
            auth=HTTPBasicAuth(
                self.user_id,
                self.api_secret),
            data=data,
            headers=headers)
        return response

    def requestToPay(
            self,
            mobile,
            amount,
            product_id,
            note="",
            message="",
            currency="EUR",
            environment="sandbox",
            **kwargs):
            # type: (String,String,String,String,String,String,String) -> json
        ref = str(uuid.uuid4())
        data = {
            "payer": {
                "partyIdType": "MSISDN",
                "partyId": mobile},
            "payeeNote": note,
            "payerMessage": message,
            "externalId": product_id,
            "currency": currency,
            "amount": amount}
        headers = {
            "X-Target-Environment": environment,
            "Content-Type": "application/json",
            "X-Reference-Id": ref,
            "Ocp-Apim-Subscription-Key": self.auth_key


        }
        url = "{0}/collection/v1_0/requesttopay".format(self.base_url)
        self.request("POST", url, headers, data)
        return {"transaction_ref": ref}

    def getBalance(self, environment="sandbox"):
        headers = {
            "X-Target-Environment": environment,
            "Content-Type": "application/json",
            "Ocp-Apim-Subscription-Key": self.auth_key
        }
        url = "{0}/collection/v1_0/account/balance".format(self.base_url)
        res = self.request("GET", url, headers)
        return res.json()

    def getTransactionStatus(
            self,
            transaction_id,
            environment="sandbox",
            **kwargs):

        headers = {
            "X-Target-Environment": environment,
            "Content-Type": "application/json",
            "Ocp-Apim-Subscription-Key": self.auth_key
        }
        url = self.base_url + "/collection/v1_0/requesttopay/" + transaction_id
        res = self.request("GET", url, headers)
        return res.json()

    def transfer(
            self,
            amount,
            mobile,
            note="",
            message="",
            currency="EUR",
            environment="sandbox",
            **kwargs):
        external_ref = str(uuid.uuid4())
        data = {
            "amount": amount,
            "currency": currency,
            "externalId": external_ref,
            "payee": {
                "partyIdType": "MSISDN",
                "partyId": mobile
            },
            "payerMessage": message,
            "payeeNote": note
        }
        headers = {
            "X-Target-Environment": environment,
            "Content-Type": "application/json",
            "Ocp-Apim-Subscription-Key": self.auth_key
        }
        url = self.base_url + "/v1_0/transfer"
        self.request("POST", url, headers, data)
        return {"transaction_ref": external_ref}

    @classmethod
    def generateToken(
            cls,
            host,
            api_user,
            api_key,
            base_url,
            environment="sandbox",
            **kwargs):
        data = {"providerCallbackHost": host}

        headers = {
            "Content-Type": "application/json",
            "Ocp-Apim-Subscription-Key": api_key,
            "X-Target-Environment": environment,
        }

        url = base_url + "/v1_0/apiuser/{0}/apikey".format(api_user)

        res = requests.post(url, data=json.dumps(data), headers=headers)
        print(res)

        return res.json()

    def close(self):
        if self._session is not None:
            print("closing!")
            self._session.close()
