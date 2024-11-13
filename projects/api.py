from .models import Project
from rest_framework import viewsets, permissions
from .serializers import ProjectSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all() # Data set
    permission_classes = [permissions.AllowAny] # Any client can view the data
    serializer_class = ProjectSerializer
