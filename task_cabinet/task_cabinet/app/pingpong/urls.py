from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'pingpong', views.PingPongViewSet, base_name='pingpong')
