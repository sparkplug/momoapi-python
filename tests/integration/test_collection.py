from pytest_bdd import scenario, given, when, then, parsers
import re
import os
import pytest
from click.testing import CliRunner
from mtnmomo.collection import Collection


pytest.globalDict = {}


@scenario('features/collections.feature', 'Request a payment from a consumer (Payer)')
def test_collections():
    pass


@given("I have a valid user_id, auth_secret, and collections subscription key")
def user_credentials():
    config = {
        "COLLECTION_USER_ID": os.environ.get("COLLECTION_USER_ID"),
        "COLLECTION_API_SECRET": os.environ.get("COLLECTION_API_SECRET"),
        "COLLECTION_PRIMARY_KEY": os.environ.get("COLLECTION_PRIMARY_KEY"),

    }
    client = Collection(config)
    pytest.globalDict["client"] = client


@when("I request for a payment with the following payment details\n| note         | amount | message | mobile     | product_id |\n| test payment | 600    | message | 0782631873 | 0001       |")
def successful_request_to_pay():

    ref = pytest.globalDict["client"].requestToPay(
        mobile="256772123456", amount="600", external_id="123456789", payee_note="dd", payer_message="dd",
        currency="EUR")
    pytest.globalDict["ref"] = ref


@when("I check for transaction Status")
def check_transaction_status():
    status = pytest.globalDict["client"].getTransactionStatus(pytest.globalDict["ref"]["transaction_ref"])
    pytest.globalDict["status"] = status
    assert isinstance(status, dict)
    assert "amount" in status.keys()
    assert "currency" in status.keys()


@then("It should be successful")
def successful_transaction():
    assert pytest.globalDict["status"]["status"] == "SUCCESSFUL"
