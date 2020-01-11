from django.conf import settings
from django.urls import path, include
from rest_framework_nested import routers

from .views import EmployerViewSet

users_router = routers.DefaultRouter(trailing_slash=False)
users_router.register(r'employers', EmployerViewSet, basename='employers')


urlpatterns = [
    path(f'{settings.API_PATH}/', include(users_router.urls)),
]
