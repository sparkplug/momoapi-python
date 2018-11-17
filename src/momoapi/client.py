import requests
import textwrap
import json
import uuid
from .errors import APIError
from requests import Request, Session
from requests.auth import AuthBase
import base64
from requests.auth import HTTPBasicAuth
from requests._internal_utils import to_native_string


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

        r.headers['Authorization'] = "Bearer "+to_native_string(self.token)
        return r


class MomoApi(object):

    def __init__(self, auth_key, user_id, api_secret, base_url="https://ericssonbasicapi2.azure-api.net", ** kwargs):
        super(MomoApi, self).__init__(**kwargs)
        self._session = Session()
        self.api_secret = api_secret
        self.user_id = user_id
        self.auth_key = auth_key
        self.base_url = base_url

    def request(self, method, url, headers, post_data=None):
        self.authToken = self.getAuthToken().json()["access_token"]
        request = Request(method,  url, data=json.dumps(post_data), headers=headers, auth=MoMoAuth("%s" % self.authToken))

        prepped = self._session.prepare_request(request)

        resp = self._session.send(prepped,
                                  verify=False
                                  )
        return self.interpret_response(resp)

    def interpret_response(self, resp):
        rcode = resp.status_code
        rheaders = resp.headers

        try:
            rbody = resp.json()
        except json.decoder.JSONDecodeError:
            rbody = resp.text
            resp = Response(rbody, rcode, rheaders)

        if not (200 <= rcode < 300):
            self.handle_error_response(rbody, rcode, resp.text, rheaders)

        return resp

    def handle_error_response(self, rbody, rcode, resp, rheaders):
        try:
            error_data = resp['error']
        except (KeyError, TypeError):
            raise APIError(
                "Invalid response object from API: %r (HTTP response code "
                "was %d)" % (rbody, rcode),
                rbody, rcode, resp)

        raise ""

    def request_headers(self, api_key, method):
        headers = {}

        return headers

    def getAuthToken(self):
        data = json.dumps({})
        auth = "%s:%s" % (self.user_id, self.api_secret)
        bs64 = base64.b64encode(auth.encode())
        headers = {
            "Content-Type": "application/json",

            "Ocp-Apim-Subscription-Key": "%s" % self.auth_key
        }
        r = requests.post(self.base_url+"/colection/token/",
                          auth=HTTPBasicAuth(self.user_id, self.api_secret), data=data, headers=headers)
        return r

    def requestToPay(self, mobile, amount, product_id, note="", message="", currency="EUR",  environment="sandbox"):
        ref = str(uuid.uuid4())
        data = {"payer": {"partyIdType": "MSISDN", "partyId": mobile}, "payeeNote": note,
                "payerMessage": message, "externalId": product_id, "currency": currency, "amount": amount}
        headers = {
            "X-Target-Environment": environment,
            "Content-Type": "application/json",
            "X-Reference-Id": ref,
            "Ocp-Apim-Subscription-Key": self.auth_key


        }
        url = self.base_url+"/colection/v1_0/requesttopay"
        res = self.request("POST", url, headers, data)
        return {"transaction_ref": ref}

    def getBalance(self, environment="sandbox"):
        headers = {
            "X-Target-Environment": environment,
            "Content-Type": "application/json",
            "Ocp-Apim-Subscription-Key": self.auth_key
        }
        url = self.base_url+"/colection/v1_0/account/balance"
        res = self.request("GET", url, headers)
        return res.json()

    def getTransactionStatus(self, transaction_id,  environment="sandbox"):

        headers = {
            "X-Target-Environment": environment,
            "Content-Type": "application/json",
            "Ocp-Apim-Subscription-Key": self.auth_key
        }
        url = self.base_url+"/colection/v1_0/requesttopay/"+transaction_id
        res = self.request("GET", url, headers)
        return res.json()

    def transfer(self, amount, mobile, note="", message="", currency="EUR", environment="sandbox"):
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
        url = self.base_url+"/v1_0/transfer"
        res = self.request("POST", url, headers, data)
        return {"transaction_ref": external_ref}

    @classmethod
    def generateToken(self, host, api_user, api_key, base_url, environment="sandbox"):
        data = {"providerCallbackHost": host}

        headers = {
            "Content-Type": "application/json",
            "Ocp-Apim-Subscription-Key": api_key,
            "X-Target-Environment": environment,
        }

        url = base_url+"/v1_0/apiuser/%s/apikey" % api_user

        res = requests.post(url, data=json.dumps({}), headers=headers)
        print(res)

        return res.json()

    def close(self):
        if self._session is not None:
            print("closing!")
            self._session.close()
