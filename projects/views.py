from projects.serializers import ProjectSerializer
from projects.models import Project
from rest_framework.viewsets import ModelViewSet

# Create your views here.
class ProjectViewSet(ModelViewSet):
    serializer_class = ProjectSerializer

    def get_queryset(self):
        return Project.objects.filter(
            removed_at__isnull=True
        )

    def perform_create(self, serializer):
        # project = Project.objects.create()
        serializer.save()