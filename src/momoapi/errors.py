
from .utils import ERROR_CODES


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
