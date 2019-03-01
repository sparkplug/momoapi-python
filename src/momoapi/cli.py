"""
Module that contains the command line app.

Why does this file exist, and why not put this in __main__?

  You might be tempted to import things from __main__ later, but that will cause
  problems: the code will get executed twice:

  - When you run `python -mmomoapi_python` python will execute
    ``__main__.py`` as a script. That means there won't be any
    ``momoapi_python.__main__`` in ``sys.modules``.
  - When you import __main__ it will get executed again (as a module) because
    there's no ``momoapi_python.__main__`` in ``sys.modules``.

  Also see (1) from http://click.pocoo.org/5/setuptools/#setuptools-integration
"""
import json
import time
import uuid

import click

import requests


def generate_token(host, key):
    data = {"providerCallbackHost": host}
    token = str(uuid.uuid4())
    headers = {
        "X-Reference-Id": token,
        "Content-Type": "application/json",
        "Ocp-Apim-Subscription-Key": key
    }

    requests.post(
        "https://ericssonbasicapi2.azure-api.net/v1_0/apiuser",
        data=json.dumps(data),
        headers=headers)
    time.sleep(5)

    del headers["X-Reference-Id"]
    url = "https://ericssonbasicapi2.azure-api.net/v1_0/apiuser/{0}/apikey".format(
        token)

    res = requests.post(url, data=json.dumps({}), headers=headers)

    rr = res.json()
    ret = {}
    if not (200 <= res.status_code < 300):
        return rr
    ret["UserId"] = token
    ret["APISecret"] = rr["apiKey"]

    return "Here is your User Id and API secret : {0}".format(ret)


@click.command()
@click.option(
    '--provider',
    prompt="providerCallBackHost",
    help='providerCallBackHost')
@click.option(
    '--key',
    prompt="Ocp-Apim-Subscription-Key",
    help='Ocp-Apim-Subscription-Key')
def main(provider, key):
    click.echo(generate_token(provider, key))
