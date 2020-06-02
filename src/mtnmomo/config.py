from .utils import validate_uuid
from .errors import ConfigurationError


class MomoConfig(object):

    def __init__(self, conf):
        """

        config={

            ENVIRONMENT: os.environ.get("ENVIRONMENT"),
            BASE_URL: os.environ.get("BASE_URL"),
            CALLBACK_HOST: os.environ.get("CALLBACK_HOST"),
            COLLECTION_PRIMARY_KEY: os.environ.get("COLLECTION_PRIMARY_KEY"),
            COLLECTION_USER_ID: os.environ.get("COLLECTION_USER_ID"),
            COLLECTION_API_SECRET: os.environ.get("COLLECTION_API_SECRET"),

            REMITTANCE_USER_ID: os.environ.get("REMITTANCE_USER_ID"),
            REMITTANCE_API_SECRET: os.environ.get("REMITTANCE_API_SECRET"),
            REMITTANCE_PRIMARY_KEY: os.environ.get("REMITTANCE_PRIMARY_KEY")

            DISBURSEMENT_USER_ID: os.environ.get("DISBURSEMENT_USER_ID"),
            DISBURSEMENT_API_SECRET: os.environ.get("DISBURSEMENTS_API_SECRET"),
            DISBURSEMENT_PRIMARY_KEY: os.environ.get("DISBURSEMENT_PRIMARY_KEY"),


        }


        """
        self._config = conf

    def get_property(self, property_name):
        if property_name not in self._config.keys():
            return None
        return self._config[property_name]

    def userId(self, product):
        key = self.get_property('{0}_USER_ID'.format(product))

        if not key:
            raise ConfigurationError(
                "{0}_USER_ID is missing in the configuration".format(product))
        else:
            return validate_uuid(key)

    def APISecret(self, product):
        key = self.get_property('{0}_API_SECRET'.format(product))

        if not key:
            raise ConfigurationError(
                "{0}_API_SECRET is missing in the configuration".format(product))
        else:
            return key

    @property
    def environment(self):
        return self.get_property('ENVIRONMENT') or "sandbox"

    @property
    def baseUrl(self):
        return self.get_property(
            'BASE_URL') or "https://ericssonbasicapi2.azure-api.net"

    @property
    def callbackHost(self):
        key = self.get_property('CALLBACK_HOST')
        if not key:
            raise ConfigurationError(
                "CALLBACK_HOST is missing in the configuration")
        else:
            return key

    @property
    def collectionsKey(self):
        key = self.get_property('COLLECTION_PRIMARY_KEY')
        if not key:
            raise ConfigurationError(
                "COLLECTION_PRIMARY_KEY is missing in the configuration")
        else:
            return validate_uuid(key)

    @property
    def disbursementsKey(self):
        key = self.get_property('DISBURSEMENT_PRIMARY_KEY')
        if not key:
            raise ConfigurationError(
                "DISBURSEMENT_PRIMARY_KEY is missing in the configuration")
        else:
            return validate_uuid(key)

    @property
    def remittencesKey(self):
        key = self.get_property('REMITTANCE_PRIMARY_KEY')
        if not key:
            raise ConfigurationError(
                "REMITTANCE_PRIMARY_KEY is missing in the configuration")
        else:
            return validate_uuid(key)
