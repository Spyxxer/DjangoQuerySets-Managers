from rest_framework import serializers
from .models import Link

class LinkSerializer(serializers.ModelSerializer):
    """Link Serializer"""

    class Meta:
        model = Link
        fields ="__all__"
        
