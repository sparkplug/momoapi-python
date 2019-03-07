from .client import MomoApi
import uuid
from .utils import validate_phone_number


class Disbursement(MomoApi):

    def getAuthToken(self):
        """
           Create an access token which can then be used to authorize and authenticate towards the other end-points of the API.
        """
        url = "/disbursement/token/"
        response = super().getAuthToken(
            "DISBURSEMENT", url, super().config.disbursementsKey)
        return response

    def getBalance(self):
        url = "/disbursement/v1_0/account/balance"

        return super().getBalance(url, super().config.disbursementsKey)

    def getTransactionStatus(
            self,
            transaction_id,
            **kwargs):
        url = "/disbursement/v1_0/transfer/"

        return super().getTransactionStatus(
            transaction_id, url, super().config.disbursementsKey)

    def transfer(
            self,
            amount,
            mobile,
            external_id,
            payee_note="",
            payer_message="",
            currency="EUR",
            **kwargs):
        ref = str(uuid.uuid4())
        data = {
            "amount": str(amount),
            "currency": currency,
            "externalId": external_id,
            "payee": {
                "partyIdType": "MSISDN",
                "partyId": validate_phone_number(mobile)
            },
            "payerMessage": payer_message,
            "payeeNote": payee_note
        }
        headers = {
            "X-Target-Environment": super().config.environment,
            "Content-Type": "application/json",
            "Ocp-Apim-Subscription-Key": super().config.disbursementsKey,
            "X-Reference-Id": ref,
        }
        if kwargs.get("callback_url"):
            headers["X-Callback-Url"] = kwargs.get("callback_url")
        url = super().config.baseUrl + "/disbursement/v1_0/transfer"
        print(url)
        self.request("POST", url, headers, data)
        return {"transaction_ref": ref}
