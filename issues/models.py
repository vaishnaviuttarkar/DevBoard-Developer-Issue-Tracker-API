from django.db import models
from django.contrib.auth.models import User
from projects.models import Project

class Issue(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    status = models.CharField(
        max_length=20,
        choices = [
            ("OPEN","Open"),
            ("CLOSED","Closed")
        ]
    )
    priority = models.CharField(
        max_length=20,
        choices = [
            ("LOW","Low"),
            ("MEDIUM","Medium"),
            ("HIGH","High"),
        ]
    )
    issue_type = models.CharField(
        max_length=20,
        choices = [
            ("BUG","Bug"),
            ("FEATURE","Feature")
        ]
    )
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name = "issues"
    )
    assigned_to = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name = "assigned_user"
    )
    created_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name = "created_user"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    removed_at = models.DateTimeField(null=True,blank=True)

    def __str__(self):
        return f"{self.title} of {self.project} assigned to {self.assigned_to}"