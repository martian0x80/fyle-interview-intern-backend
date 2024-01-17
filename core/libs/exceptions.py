class FyleError(Exception):
    status_code = 400

    def __init__(self, status_code, message):
        Exception.__init__(self)
        self.message = message
        self.status_code = status_code

    def to_dict(self):
        res = dict()
        res['message'] = self.message
        return res

# Additions start here

class FyleErrorExtended(FyleError):
    def __init__(self, message, status_code=400, error='FyleError'):
        FyleError.__init__(self, status_code, message)
        self.error = error

    def to_dict(self):
        res = FyleError.to_dict(self)
        res['data'] = self.data
        return res
    
# Additions end here