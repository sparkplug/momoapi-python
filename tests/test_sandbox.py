from pytest_bdd import scenario, given, when, then, parsers
import re
import pytest
from click.testing import CliRunner
from momoapi.cli import generateToken

pytest.globalDict = {}


@scenario('features/sandbox.feature', 'Adding new account')
def test_sanbox_provisioning():
    pass


@given(parsers.re(r'a user with the domain (?P<domain>[a-zA-Z0-9\.]+) and subscription key (?P<api_key>\w+)'),
       converters=dict(domain=str, api_key=str))
def provisioning_user(domain, api_key):

    pytest.globalDict['domain'] = domain
    pytest.globalDict['api_key'] = api_key
    return


@when('I run the command "momoapi"')
def run_command():
    return


@when('I fill in the "providerCallBackHost" with "sparkpl.ug"')
def fill_domain():
    return


@when('I fill in the "Ocp-Apim-Subscription-Key" with "99e9cb10e8c04ea0b788334dc6346f13"')
def fill_wrong_value():
    return


@when('I fill in the "Ocp-Apim-Subscription-Key" with "f83xx8d8xx6749f19a26e2265aeadbcdeg"')
def fill_key():
    return


@then('I should get the message "Access denied due to invalid subscription key"')
def wrong_key(key="f83xx8d8xx6749f19a26e2265aeadbcdeg"):
    host = pytest.globalDict["domain"]
    result = generateToken(host, key)
    assert "Access denied due to invalid subscription key" in result


@then('I should get back the apiKey')
def get_Key():

    host = pytest.globalDict["domain"]
    key = pytest.globalDict["api_key"]
    result = generateToken(host, key)
    assert "Here is your User Id and API secret" in result
