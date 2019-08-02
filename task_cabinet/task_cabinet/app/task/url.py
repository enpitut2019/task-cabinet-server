from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'task', views.TaskViewSet, base_name='task')
