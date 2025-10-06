from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLES = (
        ('admin', 'Admin'),
        ('analyst', 'Analyst'),
    )
    role = models.CharField(max_length=20, choices=ROLES, default='analyst')

    def __str__(self):
        return self.username
    
import uuid

class Campaign(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    body_template = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey('User', on_delete=models.CASCADE, related_name='campaigns')

    def __str__(self):
        return self.name


class Target(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE, related_name='targets')
    clicked = models.BooleanField(default=False)
    submitted_credentials = models.BooleanField(default=False)
    trained = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} - {self.campaign.name}"
