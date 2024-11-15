from .models import Project
from .serializers import ProjectSerializer
from rest_framework import viewsets, permissions

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all() # Consult all data from a table
    permission_classes = [permissions.AllowAny] # Any client can view the data
    serializer_class = ProjectSerializer # Transforms data
