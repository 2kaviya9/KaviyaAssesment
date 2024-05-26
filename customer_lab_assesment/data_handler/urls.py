# urls.py
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from data_handler.views import incoming_data

router = DefaultRouter()

urlpatterns = [
    path("dd/", incoming_data, name = "income_data"),
    path('', include(router.urls)),
]
