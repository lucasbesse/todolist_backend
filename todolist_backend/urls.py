from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from tasks.views import TaskViewSet, UserViewSet
from rest_framework_simplejwt.views import TokenObtainPairView

router = DefaultRouter()
router.register('tasks', TaskViewSet, basename='task')
router.register('user', UserViewSet, basename='user')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair')
]
