from django.contrib import admin
from django.urls import path
from rest_framework_swagger.views import get_swagger_view
from .app.pingpong.urls import router as pingpongRouter
from .app.task.url import router as taskRouter
from rest_framework.routers import DefaultRouter
from django.conf.urls import url, include

schema_view = get_swagger_view(title='API Lists For TaskCabinet')

router = DefaultRouter()
router.registry.extend(pingpongRouter.registry)
router.registry.extend(taskRouter.registry)

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^docs', schema_view),
    url(r'api/', include(router.urls), name='api'),
]
