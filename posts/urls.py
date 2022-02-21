from django.urls import path, include
from rest_framework_nested import routers

from .views import PostViewSet, AnalyticView

router = routers.SimpleRouter()
router.register(r"posts", PostViewSet)


urlpatterns = [
    path("", include(router.urls)),
    path(r"analytics/", AnalyticView.as_view(), name="Analytics")
]
