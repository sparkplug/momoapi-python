========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - |
        | |coveralls|
    * - package
      - | |version| |wheel| |supported-versions| |supported-implementations|
        | |commits-since|

.. |docs| image:: https://readthedocs.org/projects/python-momoapi/badge/?style=flat
    :target: https://readthedocs.org/projects/python-momoapi
    :alt: Documentation Status


.. |coveralls| image:: https://coveralls.io/repos/mossplix/python-momoapi/badge.svg?branch=master&service=github
    :alt: Coverage Status
    :target: https://coveralls.io/r/mossplix/python-momoapi

.. |version| image:: https://img.shields.io/pypi/v/momoapi-python.svg
    :alt: PyPI Package latest release
    :target: https://pypi.python.org/pypi/momoapi-python

.. |commits-since| image:: https://img.shields.io/github/commits-since/mossplix/python-momoapi/v0.1.0.svg
    :alt: Commits since latest release
    :target: https://github.com/mossplix/python-momoapi/compare/v0.1.0...master

.. |wheel| image:: https://img.shields.io/pypi/wheel/momoapi-python.svg
    :alt: PyPI Wheel
    :target: https://pypi.python.org/pypi/momoapi-python

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/momoapi-python.svg
    :alt: Supported versions
    :target: https://pypi.python.org/pypi/momoapi-python

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/momoapi-python.svg
    :alt: Supported implementations
    :target: https://pypi.python.org/pypi/momoapi-python


.. end-badges

An example package. Generated with cookiecutter-pylibrary.

* Free software: MIT license


Getting the API Key

 curl -i -X POST -H "Content-Type:application/json" -H "Ocp-Apim-Subscription-Key: 225ecdf2e0a64b069619923cee892805" -H "X-Reference-Id:f17daf51-34b3-4cfa-84c1-9b382d74aa74"  -d '{"providerCallbackHost": "sparkpl.ug"}' https://pg-all.azure-api.net/provisioning/v1_0/apiuser



curl -i -X POST -H "Content-Type:application/json" -H "Ocp-Apim-Subscription-Key: 225ecdf2e0a64b069619923cee892805"   -d '{}' https://pg-all.azure-api.net/provisioning/v1_0/apiuser/f17daf51-34b3-4cfa-84c1-9b382d74aa74/apikey



 {"apiKey":"1332ca9adc424527b442caa21b030994"}


get user

 curl  -H "Content-Type:application/json" -H "Ocp-Apim-Subscription-Key:0a30bb51ef0b4fdaa6d47c35f0b770d8"  https://pg-all.azure-api.net/provisioning/v1_0/apiuser/6a30ca37-511b-481c-bee6-005d850298c6





curl -i -X POST -H "Content-Type:application/json" -H "Ocp-Apim-Subscription-Key:0a30bb51ef0b4fdaa6d47c35f0b770d8"  -H "X-Reference-Id:6a30ca37-511b-481c-bee6-005d850298c6" -H "X-Target-Environment":"sandbox" -d '{  "payer": {"partyIdType": "MSISDN", "partyId": "1234567" }, "payeeNote": "test msg", "payerMessage": "gowl","externalId": "456","currency": "eur", "amount":"4000", }' https://pg-all.azure-api.net/collection/v1_0/requesttopay







curl -i -X POST -H "Content-Type:application/json" -H "Ocp-Apim-Subscription-Key: 225ecdf2e0a64b069619923cee892805" -H "Authorization: Basic ZjE3ZGFmNTEtMzRiMy00Y2ZhLTg0YzEtOWIzODJkNzRhYTc0OmJlOGI0MTFkZTRkZjQyOTFhNzVkOTI3N2Q2ZTIxZjc4"  -d {} https://pg-all.azure-api.net/sandboxcollection/token/






curl -i -X POST -H "Ocp-Apim-Subscription-Key: 225ecdf2e0a64b069619923cee892805" -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSMjU2In0.eyJjbGllbnRJZCI6ImYxN2RhZjUxLTM0YjMtNGNmYS04NGMxLTliMzgyZDc0YWE3NCIsImV4cGlyZXMiOiIyMDE4LTEwLTMwVDExOjUzOjI0LjYzOSIsInNlc3Npb25JZCI6IjgwMzZmNzllLWVkOTctNGNlOC1hZDk3LTY0MWE5NjY4YjE3MyJ9.dfgzIx20Nh1YP67-gMjQg6yFTD_X_judiFP3mf2XCJY9Pnvnn3erpyROJG-ZZ44iLO4tCAhS1H_-FaFgHucireQhBvs4Ztk8tTY3yg4y9ZFvq-9ks80T8cGLev1pd0fRdB1OeLqIlcvSI8fqAXU_4soDG8ObANbJImaXguKLbFLujOWG2TJcXeJ4FtlOb2_KG2uFD3_gy7-Wmh9Um85hjpNP_s_V4k354TLwwk1ODlvpahHaIafEBSiIWFEWCOV1qMgT1-c99Vwqek116eGInrray4qHr96WRsUEjCONFF4doVhQKrQECleRakKTOggXkMRnq9y6fq9mDxZ3wCwSsQ"  -H "X-Reference-Id:ca81e0b7-6fb4-41a0-97df-ce2b2da04a75" -H "X-Target-Environment:sandbox" -d '{  "payer": {"partyIdType": "MSISDN", "partyId": "2561234567" }, "payeeNote": "test msg", "payerMessage": "gowl","externalId": "67","currency": "EUR", "amount":"4000", }' https://pg-all.azure-api.net/collection/v1_0/requesttopay




"eyJ0eXAiOiJKV1QiLCJhbGciOiJSMjU2In0.eyJjbGllbnRJZCI6ImYxN2RhZjUxLTM0YjMtNGNmYS04NGMxLTliMzgyZDc0YWE3NCIsImV4cGlyZXMiOiIyMDE4LTEwLTMwVDEwOjM5OjEyLjk3NyIsInNlc3Npb25JZCI6ImY0MmQzNDFiLTNjYTItNDk2OC1iNDNiLWY5OWY0MjRlMzAwMCJ9.HN-_VNwJiqHlVzlBP2M5f2v5kTwJPV95h0ZGxEGU1DidLTC0Vn-Re-MNZqIank08tYPMtZjKb-jv7tGW7hbzHEJdL_wsgwsLHRgkoWMmPPinBAXdR7vbj1MZJXemtl3GGCpwjJHTn5LcgmItx_ZqpedWuryt_W0qNnleqUgEuI0EWPeTLQRsNwhRefEn2g4-MVkdgVY5NwIIDj2CLuiXNkng52shUXukGKYeIdqI9vV9RtPBBugqErmHivM_f6rS6ZVDTm_00RsU6auWg2wfJmTQG1JoVO4w6KKkPf-iorWr6JqhIVVu6G80VvRZzLnb7AV7yLLYsC91jFn-uRptNA"


 curl -i -X POST -H "User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36" -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSMjU2In0.eyJjbGllbnRJZCI6ImYxN2RhZjUxLTM0YjMtNGNmYS04NGMxLTliMzgyZDc0YWE3NCIsImV4cGlyZXMiOiIyMDE4LTEwLTMwVDEyOjM4OjI0LjMzMSIsInNlc3Npb25JZCI6Ijg5YjMwZTllLWMyYjQtNDY5NC04ZTg4LTIyODk2ZjBlYmRmOCJ9.T113Xi_TxLRsPfKQDb0GSjiv7iEKevS07PCzEd9DmKc9rq4AN57QnWcb_84CHO0Rq0QBUaBOWFT3eRmki0E-0K_3ZVhyTxIQadWeyUs-1ZZMTeofgq-D0K2eO7MDAW33_NidszNcWujaa0XT7a97oQWKIA7UUkiz17lHspxLi-Hai7MHhu9BJA3XxE65fOzyMQDIHfeD15B1t9_Lee4RUHo2jsWKlY6QeSiVNKaRvhAQ8G9qU9mt_uLM_XCW_zT1mhsQVg8D8SoICZ2e3kcIbuqRHTrjpWj4CXUKQzR9G8rCHz07RaYAUkPOaFFVedI2aP_Yrqtj9oJNgA-7tDN5Vw" -H "Content-Type:application/json" -H "Ocp-Apim-Subscription-Key: 225ecdf2e0a64b069619923cee892805"  -H "X-Reference-Id:f17daf51-34b3-4cfa-84c1-9b382d74aa74" -H "X-Target-Environment":"sandbox" -d '{  "payer": {"partyIdType": "MSISDN", "partyId": "256772181656" }, "payeeNote": "test msg", "payerMessage": "gowl","externalId": "456","currency": "EUR", "amount":"4000", }' https://pg-all.azure-api.net/sandboxcollection/v1_0/requesttopay


Installation
============

::

    pip install momoapi-python

Documentation
=============


https://python-momoapi.readthedocs.io/


Development
===========

To run the all tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox
