from rest_framework import routers
from .api import ProjectViewSet

router = routers.DefaultRouter() # Using this routers we avoid making by hand every route at urlpatterns

router.register('api/projects', ProjectViewSet, 'projects') # This creates a CRUD routes, 4 routes

urlpatterns = router.urls