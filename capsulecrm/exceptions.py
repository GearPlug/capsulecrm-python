class BaseError(Exception):
    pass


class UnknownError(BaseError):
    pass


class BadRequestError(BaseError):
    pass


class ValidationFailedError(BaseError):
    pass


class AuthenticationFailedError(BaseError):
    pass


class ForbiddenError(BaseError):
    pass
