from django.urls import path
from .views import IssueListAPIView, IssueDetailAPIView

urlpatterns = [
    path("issues/", IssueListAPIView.as_view()),
    path("issues/<int:pk>/", IssueDetailAPIView.as_view())
]