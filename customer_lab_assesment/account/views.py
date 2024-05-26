from requests import Response
from rest_framework.viewsets import ModelViewSet 
from rest_framework.permissions import AllowAny
from account.models import Account
from account.serializers import AccountSerializer

from rest_framework import status

class AccountViewset(ModelViewSet):
    permission_classes = (AllowAny,)
    serializer_class = AccountSerializer
    queryset = Account.objects.all()

    
# views.py
from account.serializers import MyTokenObtainPairSerializer

from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView

class LoginView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer



class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_400_BAD_REQUEST)
