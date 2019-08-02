from django.contrib import admin
from django.urls import path
from rest_framework_swagger.views import get_swagger_view
from .app.pingpong.urls import router as ping_pong_router
from .app.task.url import router as task_router
# from .app.user.urls import router as user_router
from .app.user.views import UserCreateAPIView
from rest_framework.routers import DefaultRouter,SimpleRouter
from django.conf.urls import url, include
# from draft_todo import views as dview
from task_draft import views as tview
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from task_draft.views import TaskViewSet
from user_draft.views import UserViewSet

schema_view = get_swagger_view(title='API Lists For TaskCabinet')

router = SimpleRouter()
router2 = DefaultRouter()
router2.register(r'task', TaskViewSet, base_name='task')
router.registry.extend(router2.registry)
router3 = DefaultRouter()
router3.register(r'user', UserViewSet, base_name='user')
router.registry.extend(router3.registry)

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^docs', schema_view),
    url(r'api/', include(router.urls), name='api'),
    # url(r'api-user', UserCreateAPIView.as_view(), name='api-user'),
    # url(r'draft_user/create_user', dview.TaskUserCreateAPIView.as_view(), name='dcu'),
]
