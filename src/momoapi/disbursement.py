from .client import MomoApi
import uuid
from .utils import validate_phone_number


class Disbursement(MomoApi, object):

    def getAuthToken(self):
        """
           Create an access token which can then be used to authorize and authenticate towards the other end-points of the API.
        """
        url = "/disbursement/token/"
        response = super(Disbursement, self).getAuthToken(
            "DISBURSEMENT", url, super(Disbursement, self).config.disbursementsKey)
        return response

    def getBalance(self):
        url = "/disbursement/v1_0/account/balance"

        return super(Disbursement, self).getBalance(url, super(Disbursement, self).config.disbursementsKey)

    def getTransactionStatus(
            self,
            transaction_id,
            **kwargs):
        url = "/disbursement/v1_0/transfer/"

        return super(Disbursement, self).getTransactionStatus(
            transaction_id, url, super(Disbursement, self).config.disbursementsKey)

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
            "X-Target-Environment": super(Disbursement, self).config.environment,
            "Content-Type": "application/json",
            "Ocp-Apim-Subscription-Key": super(Disbursement, self).config.disbursementsKey,
            "X-Reference-Id": ref,
        }
        if kwargs.get("callback_url"):
            headers["X-Callback-Url"] = kwargs.get("callback_url")
        url = super(Disbursement, self).config.baseUrl + "/disbursement/v1_0/transfer"
        print(url)
        self.request("POST", url, headers, data)
        return {"transaction_ref": ref}
