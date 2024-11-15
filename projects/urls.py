# urls.py APP's file
from rest_framework import routers
from .api import ProjectViewSet

router = routers.DefaultRouter() # Using routers we avoid making by hand every route at urlpatterns

# Route "api/projects", based on ProjectViewSet data, with name "projects"
router.register('api/projects', ProjectViewSet, 'projects') # This creates a CRUD routes, 4 routes in total

urlpatterns = router.urls # Adding created routes to urlpatterns