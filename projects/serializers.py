from rest_framework import serializers
from .models import Project

# This class inherits from ModelSerializer, being then a ModelSerializer.
class ProjectSerializer(serializers.ModelSerializer):
    
    # Meta class defines preferences for a model
    class Meta:
        model = Project  # ProjectSerializer will handle instances of this model

        # Fields we will be able to consult.
        fields = ('id', 'title', 'description', 'technology', 'created_at')

        read_only_fields = ('created_at',) # Not writable fields
        # Note the comma, if not placed it wouldn't be interpreted as a tuple but as a string, causing an error