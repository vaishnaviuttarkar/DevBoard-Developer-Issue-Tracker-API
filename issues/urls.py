from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import IssueListCreateAPIView, IssueDetailGenericAPIView, IssueViewSet

router = DefaultRouter()

router.register("issues", IssueViewSet, basename="issue")

# urlpatterns = [
#     path("issues/", IssueListCreateAPIView.as_view()),
#     path("issues/<int:pk>/", IssueDetailGenericAPIView.as_view())
# ]

urlpatterns = router.urls