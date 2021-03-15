# Create your views here.
from rest_framework import viewsets
from rest_framework.decorators import action
from freelancer.presenters.interators import FreelancerInterator
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_422_UNPROCESSABLE_ENTITY
)
from rest_framework.response import Response


# Register your viewsets here.
class FreelancerViewSet(viewsets.ModelViewSet):
    """
       API usando Django RestFramework
    """
    interator = FreelancerInterator()
    http_method_names = ['get', 'post']

    @action(methods=['POST'], detail=False, url_path='send-freelance', url_name='send-freelance')
    def send_freelancer(self, request):
        """
            Enpoint principal
        """
        try:
            freelancer = self.interator.set_params(request.data).execute()
            return Response(freelancer, status=HTTP_200_OK)
        except Exception as error:
            return Response(status=HTTP_422_UNPROCESSABLE_ENTITY)




