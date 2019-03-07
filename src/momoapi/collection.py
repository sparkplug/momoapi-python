import uuid

from .client import MomoApi
from .utils import validate_phone_number


class Collection(MomoApi):
    def getAuthToken(self):
        """
             Create an  access token which can then be used
        to authorize and authenticate towards the other end-points of the API
        """
        url = "/collection/token/"
        response = super().getAuthToken("COLLECTION", url, super().config.collectionsKey)
        return response

    def getBalance(self):
        url = "/collection/v1_0/account/balance"

        return super().getBalance(url, super().config.collectionsKey)

    def getTransactionStatus(
            self,
            transaction_id,
            **kwargs):
        url = "/collection/v1_0/requesttopay/"

        return super().getTransactionStatus(
            transaction_id, url, super().config.collectionsKey)

    def requestToPay(
            self,
            mobile,
            amount,
            external_id,
            payee_note="",
            payer_message="",
            currency="EUR",
            **kwargs):
            # type: (String,String,String,String,String,String,String) -> json
        ref = str(uuid.uuid4())
        data = {
            "payer": {
                "partyIdType": "MSISDN",
                "partyId": validate_phone_number(mobile)},
            "payeeNote": payee_note,
            "payerMessage": payer_message,
            "externalId": external_id,
            "currency": currency,
            "amount": str(amount)}
        headers = {
            "X-Target-Environment": super().config.environment,
            "Content-Type": "application/json",
            "X-Reference-Id": ref,
            "Ocp-Apim-Subscription-Key": super().config.collectionsKey


        }
        if kwargs.get("callback_url"):
            headers["X-Callback-Url"] = kwargs.get("callback_url")
        url = "{0}/collection/v1_0/requesttopay".format(super().config.baseUrl)
        self.request("POST", url, headers, data)
        return {"transaction_ref": ref}
