from rest_framework import serializers

from destination.models import Destination

class DestinationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Destination
        fields = "__all__"
        # extra_kwargs = {
        #     'headers': {'required': True},
        # }
