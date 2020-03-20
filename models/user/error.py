class UserError(Exception):
    def __init__(self, message):
        self.message = message


class UserNotFoundError(UserError):
    pass

class UserAlreadyregisteredError(UserError):
    pass

class InvalidEmailError(UserError):
    pass

class IncorrectPasswordError('Your password was incorrect'):
    pass