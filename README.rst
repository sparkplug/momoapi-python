## Installation

First, ensure that the you have a virtual environment enabled before you proceed. You can create one and activate as follows:

Creation of virtualenv:

```bash
$ virtualenv -p python3 <desired-path>
```

Activate the virtualenv:

```bash
$ source <desired-path>/bin/activate
```

Next, we install from source:

```bash
$ python setup.py install
```

## Requirements

* Python 2.7+ or Python 3.4+ (PyPy supported)


# Usage

Time to use the library. The goal is to create a `User ID` and `API Secret`. To do this, the API key from your profile on the MTN MoMo dashboard is needed. The library has a commandline app that helps you do just that when you enter the details as prompted on the commandline.

```bash
$ momoapi
$ providerCallBackHost: https://akabbo.ug
$ Ocp-Apim-Subscription-Key: f83xx8d8xx6749f19a26e2265aeadbcdeg
```

where `providerCallBackHost` is your callback host and `Ocp-Apim-Subscription-Key` is your account's API key. You should get the following response.

```bash
Here is your User Id and API secret : {'apiKey': 'b0431db58a9b41faa8f5860230xxxxxx', 'UserId': '053c6dea-dd68-xxxx-xxxx-c830dac9f401'}

```

## Let's make calls.

We shall now import the library onto the commandline. Let us try to make a collection request.

```python
from momoapi.client import MomoApi
client = MomoApi(APIKEY,USERID,APISECRET)
ref=client.requestToPay("256794631873", "600", "123456789", note="dd", message="dd", currency="EUR", environment="sandbox")
```
