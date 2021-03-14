from django.urls import path, include
from rest_framework.routers import DefaultRouter
from freelancer.presenters.views import FreelancerViewSet

router = DefaultRouter(trailing_slash=False)

router.register('freelancers', FreelancerViewSet, basename='freelancers')

app_name = 'freelancer'

urlpatterns = [
    path('', include(router.urls)),
]
