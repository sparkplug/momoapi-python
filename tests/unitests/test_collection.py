import unittest
import pytest
import types
try:
    from unittest import mock
except ImportError:
    import mock

from requests import Request, Session

from .utils import mocked_requests_get, mocked_requests_post, mocked_requests_session
from mtnmomo.errors import ValidationError
from mtnmomo.client import MomoApi
from mtnmomo.collection import Collection


class TestCollections(unittest.TestCase):

    @mock.patch('requests.post', side_effect=mocked_requests_post)
    def setUp(self, mock_get):
        self.config = {
            "COLLECTION_USER_ID": "0555e303-ae5b-4052-a77b-6d284cfc669c",
            "COLLECTION_API_SECRET": "API_SECRET",
            "COLLECTION_PRIMARY_KEY": "0555e303-ae5b-4052-a77b-6d284cfc669c",
            # "DISBURSEMENTS_PRIMARY_KEY": "0555e303-ae5b-4052-a77b-6d284cfc669c",
            # "REMITTENCES_PRIMARY_KEY": "0555e303-ae5b-4052-a77b-6d284cfc669c"
        }
        client = Collection(self.config)
        self.client = client

    def tearDown(self):
        pass
        # self.widget.dispose()
        #self.widget = None

    @mock.patch('requests.get', side_effect=mocked_requests_get)
    def test_client_instantiate(self, mock_get):

        client = Collection(self.config)

        #request_mock.assert_requested("post", "/v1/accounts")
        assert isinstance(client, Collection)

    @mock.patch('requests.get', side_effect=mocked_requests_get)
    def test_invalid_uuid(self, mock_get):
        #client = MomoApi("APIKEY", "USERID", "APISECRET")
        with self.assertRaises(ValidationError):
            config = self.config
            config["COLLECTION_PRIMARY_KEY"] = "invalid key"
            client = Collection(config)
            client.getAuthToken()

    @mock.patch('requests.get', side_effect=mocked_requests_get)
    def test_invalid_mobile(self, mock_get):
        #client = MomoApi("APIKEY", "USERID", "APISECRET")
        with self.assertRaises(ValidationError):
            ref = self.client.requestToPay(mobile="256712123456", amount="600",
                                           external_id="123456789", payee_note="dd", payer_message="dd", currency="EUR")
        with self.assertRaises(ValidationError):
            ref = self.client.requestToPay(mobile="254712123456", amount="600",
                                           external_id="123456789", payee_note="dd", payer_message="dd", currency="EUR")

    @mock.patch.object(MomoApi, "request", side_effect=mocked_requests_session)
    def test_request_to_pay(self, mock_get):

        ref = self.client.requestToPay(mobile="256772123456", amount="600", external_id="123456789", payee_note="dd",
                                       payer_message="dd", currency="EUR")

        assert isinstance(ref, dict)
        assert "transaction_ref" in ref.keys()

    @mock.patch.object(MomoApi, "request", side_effect=mocked_requests_session)
    def test_get_balance(self, mock_get):
        balance = self.client.getBalance()
        assert isinstance(balance, dict)
        assert "availableBalance" in balance.keys()
        assert "currency" in balance.keys()

    # @mock.patch('requests.get', side_effect=mocked_requests_get)
    @mock.patch.object(MomoApi, "request", side_effect=mocked_requests_session)
    def test_get_transaction_status(self, mock_get):
        status = self.client.getTransactionStatus("dummy")
        assert isinstance(status, dict)
        assert "amount" in status.keys()
        assert "currency" in status.keys()

    # @mock.patch.object(MomoApi, "request", side_effect=mocked_requests_session)
    # def test_transfer(self, mock):
        # ref = self.client.transfer("600", "256772123456", note="dd",
        # message="dd", currency="EUR", environment="sandbox")
        #assert isinstance(ref, dict)
        #assert "transaction_ref" in ref.keys()

    @mock.patch('requests.post', side_effect=mocked_requests_post)
    def test_generate_token(self, mock):
        res = MomoApi.generateToken("dummy_host", "dummy_user", "dummy_key", "dummy_base")
        assert isinstance(res, dict)
        assert "apiKey" in res.keys()
