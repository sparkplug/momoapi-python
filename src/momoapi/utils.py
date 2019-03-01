
from phonenumbers import carrier
import phonenumbers

ERROR_CODES = [
    {
        "http_code": 409,
        "response_code": None,
        "description": "Duplicated Reference Id. Cannot create new resource",
        "error_type": "generic"

    },
    {
        "http_code": 404,
        "response_code": None,
        "description": "Reference Id not found. Requested resource does not exist",
        "error_type": "generic"

    },
    {
        "http_code": 400,
        "response_code": None,
        "description": "Bad request. Request does not follow the specification.",
        "error_type": "generic"

    },
    {
        "http_code": 401,
        "response_code": None,
        "description": "Authentication failed. Credentials not valid",
        "error_type": "generic"

    },

    {
        "http_code": 500,
        "response_code": "NOT_ALLOWED",
        "description": "Authorization failed. User does not have permission.",
        "error_type": "generic"

    },

    {
        "http_code": 500,
        "response_code": "NOT_ALLOWED_TARGET_ENVIRONMENT",
        "description": "Not allowed target environment",
        "error_type": "generic"

    },

    {
        "http_code": 500,
        "response_code": "INVALID_CALLBACK_URL_HOST",
        "description": "Callback URL with different host name then configured for API User",
        "error_type": "generic"

    },

    {
        "http_code": 500,
        "response_code": "INVALID_CURRENCY",
        "description": "Currency not supported on the requested account",
        "error_type": "generic"

    },

    {
        "http_code": 500,
        "response_code": "INTERNAL_PROCESSING_ERROR",
        "description": "Default error code used when there is no specific error mapping.",
        "error_type": "generic"

    },

    {
        "http_code": 500,
        "response_code": "SERVICE_UNAVAILABLE",
        "description": "Service temporary unavailable, try again later",
        "error_type": "generic"

    },

    {
        "http_code": 500,
        "response_code": "PAYER_NOT_FOUND",
        "description": "Payer not found",
        "error_type": "preapproval"

    },

    {
        "http_code": 500,
        "response_code": "PAYEE_NOT_ALLOWED_TO_RECEIVE",
        "description": "Payee cannot receive funds due to e.g. transfer limit.",
        "error_type": "request_to_pay"

    },

    {
        "http_code": 500,
        "response_code": "NOT_ENOUGH_FUNDS",
        "description": "Not enough funds on payer account",
        "error_type": "transfer"

    },
    {
        "http_code": 500,
        "response_code": "PAYER_LIMIT_REACHED",
        "description": "Not allowed to end due to Payer limit reached",
        "error_type": "transfer"

    },

    {
        "http_code": 500,
        "response_code": "PAYEE_NOT_FOUND",
        "description": "Payee not found. Account holder is not registered",
        "error_type": "transfer"

    },

    {
        "http_code": 404,
        "response_code": None,
        "description": "Account holder is not found",
        "error_type": "account"

    }
]


def requests_retry_session(
    retries=3,
    backoff_factor=0.3,
    status_forcelist=(502, 504),
    session=None,
):
    session = session or requests.Session()
    retry = Retry(
        total=retries,
        read=retries,
        connect=retries,
        backoff_factor=backoff_factor,
        status_forcelist=status_forcelist,
    )
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('http://', adapter)
    session.mount('https://', adapter)
    return session


def validate_phone_number(number):
    obj = phonenumbers.parse(number, "UG")
    if (phonenumbers.is_valid_numbe(obj) == False):
        raise Exception("Invalid Phone number %s" % number)
    if (carrier.name_for_number(obj, "en") != "MTN"):
        raise Exception("%s: Only MTN is supported at the moment" % number)
    return "256" + obj.national_number


def validate_number(number):
    number_types = (int, float)
    if sys.version_info < (3, 0, 0):
        number_types += (long,)
    if not type(number) in number_types:
        raise Exception("%s: Must be a number" % number)
    return number


def validate_string(_string):
    if not type(_string) == str:
        raise Exception("%s: Must be a string" % _string)
    return string
