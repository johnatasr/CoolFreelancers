from django.shortcuts import render
from ninja import NinjaAPI
from typing import List
from .scheme import Freelancer

api = NinjaAPI()


class ApiCoolfreela():

    def __init__(self):
        ...

    @api.get("/search-freelancers")
    def search_freelancer(self, freelancer: Freelancer):
        try:
            valid: bool = payload_validator(freelancer)

            if(valid):
                results = process_search(freelancer)
                return results
            else:
                raise PayloadExcption

        except Exception as error:
            raise error



