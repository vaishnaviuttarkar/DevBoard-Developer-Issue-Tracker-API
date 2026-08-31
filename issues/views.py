from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.contrib.auth.models import User
from issues.models import Issue
from issues.serializers import IssueSerializer

class IssueListAPIView(APIView):

    def get(self,request):
        issues = Issue.objects.filter(
            removed_at__isnull=True
        ).select_related("project")

        serializer = IssueSerializer(issues,many=True)

        return Response(serializer.data)

    def post(self,request):
        serializer = IssueSerializer(data=request.data)

        user = User.objects.get(username="vaishnavi")
        if serializer.is_valid():
            serializer.save(created_by=user)

            return Response(
                serializer.data,
                status = status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status = status.HTTP_400_BAD_REQUEST
        )


class IssueDetailAPIView(APIView):
    def get_object(self,pk):
        try:
            issue = Issue.objects.get(id=pk)
            return issue
        except Issue.DoesNotExist:
                return None

    def get(self, request, pk):
        issue = self.get_object(pk)

        if issue is None:
            return Response(
                {"detail": "Issue not found"},
                status= status.HTTP_404_NOT_FOUND
            )

        serializer = IssueSerializer(issue)

        return Response(serializer.data)

    def put(self, request, pk):
        issue = self.get_object(pk)

        if issue is None:
            return Response(
                {"detail": "Issue not found"},
                status= status.HTTP_404_NOT_FOUND
            )
        
        serializer = IssueSerializer(issue, data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(
                serializer.data,
                status=status.HTTP_200_OK
            )

        return Response(
            serializer.errors,
            status= status.HTTP_400_BAD_REQUEST
        )

    def patch(self, request, pk):
        issue = self.get_object(pk)

        if issue is None:
            return Response(
                {"detail": "Issue not found"},
                status= status.HTTP_404_NOT_FOUND
            )
        
        serializer = IssueSerializer(issue, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()

            return Response(
                serializer.data,
                status=status.HTTP_200_OK
            )

        return Response(
            serializer.errors,
            status= status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, pk):
        issue = self.get_object(pk)
        
        if issue is None:
            return Response(
                {"detail": "Issue not found"},
                status= status.HTTP_404_NOT_FOUND
            )

        issue.delete()

        return Response(
            {"detail": "Issue deleted successfully"},
            status=status.HTTP_204_NO_CONTENT
        )