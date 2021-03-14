class CoolFreelaException(Exception):

    def __init__(self, source, code, message):
        super().__init__(message)
        self._source = source
        self._code = code

    @property
    def source(self):
        return self._source

    @property
    def code(self):
        return self._code


class InvalidPayloadException(CoolFreelaException):
    pass


class ConflictException(CoolFreelaException):
    pass




class EntityDoesNotExistException(CoolFreelaException):

    def __init__(self, entity):
        super().__init__(source='entity', code='not_found', message=f'Entidade: {entity} não encotrada ')


class NoPermissionException(CoolFreelaException):

    def __init__(self):
        super().__init__(source='permission', code='denied', message='Permission denied')