from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
# Create your models here.
#createing client model
class Client(models.Model):
    client_id = models.AutoField(primary_key=True)
    client_name = models.CharField(max_length=100)
    created_by = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=now)

    class Meta:
        db_table = "clients"

    def __str__(self):
        return self.client_name


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=100)
    user_email = models.EmailField(max_length=100)
    user_password = models.CharField(max_length=100)

    class Meta:
        db_table = "users"

    def __str__(self):
        return self.user_name


class Project(models.Model):
    project_id = models.AutoField(primary_key=True)
    project_name = models.CharField(max_length=100)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="projects")
    users = models.ManyToManyField(User, related_name="projects")
    created_by = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=now)

    class Meta:
        db_table = "projects"

    def __str__(self):
        return self.project_name