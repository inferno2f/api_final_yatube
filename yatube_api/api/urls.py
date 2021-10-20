from django.urls.conf import include
from rest_framework import routers

from django.urls import path

from .views import PostViewSet


router = routers.DefaultRouter()
router.register(r'posts', PostViewSet)

app_name = 'api'

urlpatterns = [
    path('v1/', include(router.urls)),
]
