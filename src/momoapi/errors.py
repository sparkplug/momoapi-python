

class MomoError(Exception):
    def __init__(self, message=None, http_body=None, http_status=None,
                 json_body=None, headers=None, code=None):
        super(MomoError, self).__init__(message)

        if http_body and hasattr(http_body, 'decode'):
            try:
                http_body = http_body.decode('utf-8')
            except BaseException:
                http_body = ('<Could not decode body as utf-8. ')

        self._message = message
        self.http_body = http_body
        self.http_status = http_status
        self.json_body = json_body
        self.headers = headers or {}
        self.code = code
        self.request_id = self.headers.get('request-id', None)

    def __str__(self):
        msg = self._message or "<empty message>"
        if self.request_id is not None:
            return u"Request {0}: {1}".format(self.request_id, msg)
        else:
            return msg

    # Returns the underlying `Exception` (base class) message

    @property
    def user_message(self):
        return self._message

    def __repr__(self):
        return '%s(message=%r, http_status=%r, request_id=%r)' % (
            self.__class__.__name__,
            self._message,
            self.http_status,
            self.request_id)



class APIError(MomoError):
    pass

class APIConnectionError(MomoError):
    pass

class AuthenticationError(MomoError):
    pass


class PermissionError(MomoError):
    pass

class PreapprovalError(MomoError):
    pass

class RequestToPayError(MomoError):
    pass

class TransferError(MomoError):
    pass

class GeneralError(MomoError):
    pass


ERROR_CODES= [
    {
    "http_code": 409,
    "response_code":None,
    "description": "Duplicated Reference Id. Cannot create new resource",
    "error_type": "generic"

    },
    {
    "http_code": 404,
    "response_code":None,
    "description": "Reference Id not found. Requested resource does not exist",
    "error_type": "generic"

    },
     {
    "http_code": 400,
    "response_code":None,
    "description": "Bad request. Request does not follow the specification.",
    "error_type": "generic"

    },
        {
    "http_code": 401,
    "response_code":None,
    "description": "Authentication failed. Credentials not valid",
    "error_type": "generic"

    },

    {
    "http_code": 500,
    "response_code":"NOT_ALLOWED",
    "description": "Authorization failed. User does not have permission.",
    "error_type": "generic"

    },

      {
    "http_code": 500,
    "response_code":"NOT_ALLOWED_TARGET_ENVIRONMENT",
    "description": "Not allowed target environment",
    "error_type": "generic"

    },

     {
    "http_code": 500,
    "response_code":"INVALID_CALLBACK_URL_HOST",
    "description": "Callback URL with different host name then configured for API User",
    "error_type": "generic"

    },

     {
    "http_code": 500,
    "response_code":"INVALID_CURRENCY",
    "description": "Currency not supported on the requested account",
    "error_type": "generic"

    },

    {
    "http_code": 500,
    "response_code":"INTERNAL_PROCESSING_ERROR",
    "description": "Default error code used when there is no specific error mapping.",
    "error_type": "generic"

    },

      {
    "http_code": 500,
    "response_code":"SERVICE_UNAVAILABLE",
    "description": "Service temporary unavailable, try again later",
    "error_type": "generic"

    },

     {
    "http_code": 500,
    "response_code":"PAYER_NOT_FOUND",
    "description": "Payer not found",
    "error_type": "preapproval"

    },

         {
    "http_code": 500,
    "response_code":"PAYEE_NOT_ALLOWED_TO_RECEIVE",
    "description": "Payee cannot receive funds due to e.g. transfer limit.",
    "error_type": "request_to_pay"

    },

      {
    "http_code": 500,
    "response_code":"NOT_ENOUGH_FUNDS",
    "description": "Not enough funds on payer account",
    "error_type": "transfer"

    },
    {
    "http_code": 500,
    "response_code":"PAYER_LIMIT_REACHED",
    "description": "Not allowed to end due to Payer limit reached",
    "error_type": "transfer"

    },

     {
    "http_code": 500,
    "response_code":"PAYEE_NOT_FOUND",
    "description": "Payee not found. Account holder is not registered",
    "error_type": "transfer"

    },

        {
    "http_code": 404,
    "response_code":None,
    "description": "Account holder is not found",
    "error_type": "account"

    }
]
