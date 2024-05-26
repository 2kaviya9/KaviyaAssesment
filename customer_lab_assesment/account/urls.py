from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import AccountViewset

from account.views import LoginView
router = DefaultRouter()
router.register(r'account', AccountViewset, basename="account")

urlpatterns = [
    
    path("login/", LoginView.as_view(), name="token_obtain_pair"),
    path('', include(router.urls)),
]



