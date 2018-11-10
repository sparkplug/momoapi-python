## Documentation

## Installation


Install from source with:

    python setup.py install

### Requirements

* Python 2.7+ or Python 3.4+ (PyPy supported)



#Usage

The library needs to be configured with your account's api key which is
available in your [MOMOAPI Dashboard] Profile





# The library includes a commandline app to help you generate the Sandbox Auth Secret and UserId

```console
foo@bar:~$ momoapi
foo@bar:~$ providerCallBackHost:
foo.com
foo@bar:~$ Ocp-Apim-Subscription-Key:
```

where providerCallBackHost  is your callback host


and  Ocp-Apim-Subscription-Key is your account's API key

This will give you
```console
Here is your User Id and API secret : {'apiKey': 'b0431db58a9b41faa8f5860230d81752', 'UserId': '053c6dea-dd68-4501-b2ef-c830dac9f401'}

```


### Request To Pay


``` python
 from momoapi.client import MomoApi

  client = MomoApi(APIKEY,USERID,APISECRET)






# Request To Pay

    ref=client.requestToPay("256794631873", "600", "123456789", note="dd", message="dd", currency="EUR",
   environment="sandbox"
   )
   #returns transaction refernec


```



