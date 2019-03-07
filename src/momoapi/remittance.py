from .client import MomoApi
import uuid
from .utils import validate_phone_number


class Remittance(MomoApi):
    def getAuthToken(self):
        """Generate access token which can then be use to authorize and authenticate towards the other end-points of the API"""

        url = "/remittance/token/"
        response = super().getAuthToken("REMITTANCE", url, super().config.remittencesKey)
        return response

    def getBalance(self):
        url = "/remittance/v1_0/account/balance"
        return super().getBalance(url, super().config.remittencesKey)

    def getTransactionStatus(
            self,
            transaction_id,
            **kwargs):
        """
          get the status of a transfer
        """
        url = "/remittance/v1_0/transfer/"

        return super().getTransactionStatus(
            transaction_id, url, super().config.remittencesKey)

    def transfer(
            self,
            amount,
            mobile,
            external_id,
            payer_message,
            payee_note,
            currency="EUR",
            **kwargs):
        """
         Transfer operation is used to transfer an amount from the own account to
        a payee account

        """

        ref = str(uuid.uuid4())
        data = {
            "amount": str(amount),
            "currency": currency,
            "externalId": external_id,
            "payee": {
                "partyIdType": "MSISDN",
                "partyId": validate_phone_number(mobile)},

            "payerMessage": payer_message,
            "payeeNote": payee_note
        }

        headers = {
            "X-Target-Environment": super().config.environment,
            "Content-Type": "application/json",
            "X-Reference-Id": ref,
            "Ocp-Apim-Subscription-Key": super().config.remittencesKey

        }

        if kwargs.get("callback_url"):
            headers["X-Callback-Url"] = kwargs.get("callback_url")

        url = "{0}/remittance/v1_0/transfer".format(super().config.baseUrl)
        self.request("POST", url, headers, data)
        return {"transaction_ref": ref}

    def isActive(self, mobile):
        """
        Operation is used  to check if an account holder is registered and
        active in the system

        """

        headers = {
            "X-Target-Environment": self.config.environment,
            "Content-Type": "application/json",
            "Ocp-Apim-Subscription-Key": super().config.remittencesKey
        }
        url = "{0}/remittance/v1_0/accountholder/MSISDN/{1}/active".format(
            super().config.baseUrl, mobile)
        res = self.request("GET", url, headers)
        return res.json()
