class CoolFreelaException(Exception):
    """
        Exception base da aplicacao
    """
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
    """
       Exception para o modula de validacao
    """
    pass


class ConflictException(CoolFreelaException):
    """
        Exception para conflitos gerais
    """
    pass


class InteratorException(CoolFreelaException):
    """
          Exception para o modula de interacao
    """
    def __init__(self, process):
        super().__init__(source='interator', code='error', message=f"Erro em : {process}")


class EntityDoesNotExistException(CoolFreelaException):
    """
        Exception para o modula de entidades
    """

    def __init__(self, entity):
        super().__init__(source='entity', code='not_found', message=f'Entidade: {entity} não encotrada ')


class NoPermissionException(CoolFreelaException):
    """
        Exception para o modula de seguranca
    """
    def __init__(self):
        super().__init__(source='permission', code='denied', message='Permission denied')