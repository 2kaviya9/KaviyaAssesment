from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .models import Destination
from .serializers import DestinationSerializer

class DestinationViewset(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer
