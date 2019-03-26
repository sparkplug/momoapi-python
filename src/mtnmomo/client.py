"""
Base implementation of the MTN API client

@author: Moses Mugisha
"""
import json
try:
    from json.decoder import JSONDecodeError
except ImportError:
    JSONDecodeError = ValueError

import requests
from requests import Request, Session
from requests._internal_utils import to_native_string
from requests.auth import AuthBase
from requests.auth import HTTPBasicAuth


from .config import MomoConfig
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


class ClientInterface():
    def getAuthToken(self):
        raise NotImplementedError

    def getBalance(self):
        raise NotImplementedError

    def getTransactionStatus(self):
        raise NotImplementedError


class Client(ClientInterface):
    def getAuthToken(self):
        return super(Client, self).getAuthToken()

    def getBalance(self):
        return super(Client, self).getBalance()

    def getTransactionStatus(self):
        return super(Client, self).getTransactionStatus()


class MomoApi(ClientInterface, object):

    def __init__(
            self,
            config,
            ** kwargs):
        super(MomoApi, self).__init__(**kwargs)
        self._session = Session()
        self._config = MomoConfig(config)

    @property
    def config(self):
        return self._config

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
        print(resp)

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

    def getAuthToken(self, product, url, subscription_key):
        data = json.dumps({})
        headers = {
            "Content-Type": "application/json",
            "Ocp-Apim-Subscription-Key": subscription_key
        }
        response = requests.post(

            "{0}{1}".format(self.config.baseUrl, url),
            auth=HTTPBasicAuth(
                self.config.userId(product),
                self.config.APISecret(product)),
            data=data,
            headers=headers)
        return response

    def getBalance(self, url, subscription_key):
        headers = {
            "X-Target-Environment": self.config.environment,
            "Content-Type": "application/json",
            "Ocp-Apim-Subscription-Key": subscription_key
        }
        url = "{0}{1}".format(self.config.baseUrl, url)
        res = self.request("GET", url, headers)
        return res.json()

    def getTransactionStatus(
            self,
            transaction_id,
            url,
            subscription_key,
            ** kwargs):

        headers = {
            "X-Target-Environment": self.config.environment,
            "Content-Type": "application/json",
            "Ocp-Apim-Subscription-Key": subscription_key
        }
        _url = self.config.baseUrl + url + transaction_id
        print(_url)
        res = self.request("GET", _url, headers)
        return res.json()

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

        return res.json()

    def close(self):
        if self._session is not None:
            print("closing!")
            self._session.close()
