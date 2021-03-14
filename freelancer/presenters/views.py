# Create your views here.
from rest_framework import viewsets
from rest_framework.decorators import action
from freelancer.presenters.interators import FreelancerInterator
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_500_INTERNAL_SERVER_ERROR,
    HTTP_422_UNPROCESSABLE_ENTITY
)
from rest_framework.response import Response
from ninja import NinjaAPI

api = NinjaAPI()


# Register your viewsets here.
class FreelancerViewSet(viewsets.ModelViewSet):
    """
       Está API é sincrona usando Django RestFramework
    """
    interator = FreelancerInterator()
    http_method_names = ['get', 'post']

    @action(methods=['POST'], detail=False, url_path='send-freelance', url_name='send-freelance')
    def get_markers(self, request):
        try:
            freelancer = self.interator.set_params(request.data).execute()
            return Response(freelancer, status=HTTP_200_OK)
        except Exception as error:
            return Response(error, status=HTTP_422_UNPROCESSABLE_ENTITY)


# class ApiSearchFreelancer():
#
#     def __init__(self):
#         ...
#
#     @api.get("/search-freelancers")
#     def search_freelancer(self, freelancer: Freelancer):
#         try:
#             valid: bool = payload_validator(freelancer)
#
#             if(valid):
#                 results = process_search(freelancer)
#                 return results
#             else:
#                 raise PayloadExcption
#
#         except Exception as error:
#             raise error



