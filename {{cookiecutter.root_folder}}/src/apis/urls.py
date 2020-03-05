from accounts.apis import apps as account_apps, LogoutView, LoginView
from django.urls import path

from rest_framework.routers import DefaultRouter


api_routers = DefaultRouter()


def register_apis(resources):
    if resources:
        for resource in resources:
            resource_name = resource.resource_name
            api_routers.register(resource_name, resource, resource_name)

# register for each API
register_apis(account_apps)

# Collect all end-point patterns
urlpatterns = [
    path('logout/', LogoutView.as_view()),
    path('login/', LoginView.as_view()),
]

urlpatterns += api_routers.urls
