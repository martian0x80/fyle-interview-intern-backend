from flask import Response, jsonify, make_response
from core.libs.exceptions import FyleErrorExtended

class APIResponse(Response):
    @classmethod
    def respond(cls, data):
        return make_response(jsonify(data=data))


class APIError(Response):
    @classmethod
    def respond(cls, error: 'FyleErrorExtended'):
        return make_response(jsonify(error=error.error, message=error.message), error.status_code)
    