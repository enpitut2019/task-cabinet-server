from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter,SimpleRouter
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from task_draft.views import TaskViewSet, TaskAuthUserAPIView
from user_draft.views import UserViewSet
from task_draft.views import TaskAuthUserCreateTodoItemAPIView

router = SimpleRouter()
task_router = DefaultRouter()
task_router.register(r'task', TaskViewSet, base_name='task')
router.registry.extend(task_router.registry)
user_router = DefaultRouter()
user_router.register(r'user', UserViewSet, base_name='user')
router.registry.extend(user_router.registry)
task_auth_router = DefaultRouter()
task_auth_router.register(r'authuser', TaskAuthUserAPIView)
router.registry.extend(task_auth_router.registry)

schema_view = get_schema_view(
   openapi.Info(
      title="RESTful API Lists For TaskCabinet",
      default_version='v1',
      description="TaskCabinet Server",
      terms_of_service="https://github.com/enpitut2019/task-cabinet-server",
      license=openapi.License(name="MIT"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^redoc/$',
        schema_view.with_ui('redoc', cache_timeout=0),
        name='schema-redoc'),
    path(r'api/', include(router.urls), name='api'),
    path('draft_authuser/create_task',
         TaskAuthUserCreateTodoItemAPIView.as_view(),
        name='dact'),
]