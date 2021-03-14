from typing import Type
from abc import ABC, abstractmethod
# from src.presenters.helpers import HttpRequest, HttpResponse


class IValidator(ABC):
    """ Interface para o Validator"""

    @abstractmethod
    def valid(self, value: bool) -> bool:
        raise Exception("Deve implementar o método: valid")

    @abstractmethod
    def is_empty_payload(self) -> None:
        raise Exception("Deve implementar o método: is_empty_payload")

    @abstractmethod
    def validate_payload(self) -> (bool, dict):
        raise Exception("Deve implementar o método: validate_payload")


class IIterator(ABC):
    """ Interface para o Interator """

    @abstractmethod
    def set_params(self, *args, **kwargs):
        raise Exception("Deve implementar o método: set_params")

    @abstractmethod
    def execute(self, *args, **kwargs):
        raise Exception("Deve implementar o método: execute")


# class IApi(ABC):
#     """ Interface para a Api com Django Ninja"""
#
#     @abstractmethod
#     def get(self, http_request: Type[HttpRequest]) -> HttpResponse:
#         """ Defining Route """
#
#         raise Exception("Should implement method: route")
#
#     @abstractmethod
#     def post(self, http_request: Type[HttpRequest]) -> HttpResponse:
#         """ Defining Route """
#
#         raise Exception("Should implement method: route")