# coding=utf-8
from __future__ import absolute_import

import http
from .base import APIError


# not found
class NotFound(APIError):
    status_code = http.client.NOT_FOUND
    status_message = 'RESOURCE_NOT_FOUND'
    response_code = 100000


# forbidden
class PermissionDenied(APIError):
    status_code = http.client.FORBIDDEN
    status_message = 'FORBIDDEN'
    response_code = 101000


class PermissionExpired(PermissionDenied):
    status_message = 'EXPIRED'
    response_code = 101001


# unauthorized
class AuthFailed(APIError):
    status_code = http.client.UNAUTHORIZED
    status_message = 'AUTHENTICATION_FAILED'
    response_code = 102000


# not allow
class MethodNotAllowed(APIError):
    status_code = http.client.METHOD_NOT_ALLOWED
    status_message = 'REQUEST_METHOD_NOT_ALLOWED'
    response_code = 103000


# bad request
class BadRequest(APIError):
    status_code = http.client.BAD_REQUEST
    status_message = 'BAD_REQUEST'
    response_code = 104000


class RequestBodyNotExists(BadRequest):
    response_code = 104001
    status_message = "REQUEST_BODY_NOT_EXISTS"


class InvalidRequestBody(BadRequest):
    response_code = 104002
    status_message = "INVALID_REQUEST_BODY"


class RequestMaxLimited(BadRequest):
    response_code = 104003
    status_message = "REQUEST_REACHES_MAX_LIMIT"


class RequestBlocked(BadRequest):
    response_code = 104004
    status_message = "REQUEST_BLOCKED"


# internal server error
class InternalServerError(APIError):
    status_code = http.client.INTERNAL_SERVER_ERROR
    response_code = 105000
    status_message = "INTERNAL_SERVER_ERROR"


class ResponseInstanceTypeError(InternalServerError):
    response_code = 105001
    status_message = "API_RESPONSE_TYPE_ERROR"


class UncaughtException(InternalServerError):
    response_code = 105002
    status_message = "UNCAUGHT_EXCEPTION"


class MongoDBError(InternalServerError):
    response_code = 105003
    status_message = "MONGODB_ERROR"


# conflict
class ConflictError(APIError):
    status_code = http.client.CONFLICT
    status_message = 'CONFLICT_ERROR'
    response_code = 106000


# unexpection
class Unexpected(APIError):
    status_code = http.client.EXPECTATION_FAILED
    status_message = 'UNEXPECTED'
    response_code = 107000


class ValidationError(Unexpected):
    response_code = 107001
    status_message = 'INVALID_DATA'
