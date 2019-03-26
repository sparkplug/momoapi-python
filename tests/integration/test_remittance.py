from pytest_bdd import scenario, given, when, then, parsers
import re
import os
import pytest
from click.testing import CliRunner

from mtnmomo.cli import generateToken
from mtnmomo.remittance import Remittance

pytest.globalDict = {}


@scenario('features/remittances.feature', 'Move money from one account to another')
def test_remittences():
    pass


@given("I have a valid user_id, auth_secret, and remittence subscription key")
def user_credentials():
    config = {
        "REMITTANCE_USER_ID": os.environ.get("REMITTANCE_USER_ID"),
        "REMITTANCE_API_SECRET": os.environ.get("REMITTANCE_API_SECRET"),
        "REMITTANCE_PRIMARY_KEY": os.environ.get("REMITTANCE_PRIMARY_KEY"),
    }
    client = Remittance(config)
    pytest.globalDict["client"] = client


@when("I transfer with  the following details\n| note         | amount | message | mobile     | product_id |\n| test payment | 600    | message | 0782631873 | 0001       |")
def successful_transfer():
    ref = pytest.globalDict["client"].transfer(
        amount="600", mobile="256772123456", external_id="123456789", payee_note="dd", payer_message="dd",
        currency="EUR")
    pytest.globalDict["ref"] = ref

    assert isinstance(ref, dict)
    assert "transaction_ref" in ref.keys()


@when("I check for transaction Status")
def check_transaction_status():
    status = pytest.globalDict["client"].getTransactionStatus(pytest.globalDict["ref"]["transaction_ref"])
    pytest.globalDict["status"] = status
    assert isinstance(status, dict)
    assert "amount" in status.keys()
    assert "currency" in status.keys()


@then("It should be successful")
def sucessful_transaction():
    assert pytest.globalDict["status"]["status"] == "SUCCESSFUL"
