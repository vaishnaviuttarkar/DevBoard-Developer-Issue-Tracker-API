from projects.serializers import ProjectSerializer
from projects.models import Project
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from django.core.cache import cache
from django.utils import timezone
import time

# Create your views here.
class ProjectViewSet(ModelViewSet):
    serializer_class = ProjectSerializer

    def get_queryset(self):
        return Project.objects.filter(
            removed_at__isnull=True
        )

    def list(self, request, *args, **kwargs):
        cache_key = "project:list"

        start = time.perf_counter()

        cached_data = cache.get(cache_key)

        if cached_data is not None:
            print("CACHE HIT")
            print("Cache response time:", (time.perf_counter() - start) * 1000, "ms")
            return Response(cached_data)

        print("CACHE MISS")
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset,many=True)
        data = serializer.data

        cache.set(cache_key, data, timeout=300)

        return Response(data)

    def perform_create(self, serializer):
        serializer.save()
        cache.delete("projects:list")

    def perform_update(self, serializer):
        serializer.save()
        cache.delete("projects:list")

    def perform_destroy(self, instance):
        instance.removed_at = timezone.now()
        instance.save()
        cache.delete("projects:list")