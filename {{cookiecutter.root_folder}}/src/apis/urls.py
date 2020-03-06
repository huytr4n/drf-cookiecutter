from importlib import import_module
from django.conf import settings
from django.urls import path
from rest_framework.routers import DefaultRouter

from accounts.apis import LogoutView, LoginView


# Create root API router.
api_routers = DefaultRouter()

# Load all api apps from settings.
api_apps = settings.API_APPS

for api_app in api_apps:
    api_module = import_module(f'{api_app}.apis', 'apps')
    for viewset in api_module.apps:
        api_routers.register(
            viewset.resource_name,
            viewset,
            viewset.resource_name,
        )

# Collect all end-point patterns
urlpatterns = [
    path('logout/', LogoutView.as_view()),
    path('login/', LoginView.as_view()),
]

urlpatterns += api_routers.urls
