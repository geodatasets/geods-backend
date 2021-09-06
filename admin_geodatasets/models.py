from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import Model
# Create your models here.

class Project (models.Model):
    id = models.BigAutoField(primary_key=True)
    slug = models.CharField(max_length=150,unique=True)
    title = models.CharField(max_length=250)
    visibility = models.CharField(max_length=50, choices=[
        ("public","Public"),("private","Private")
    ])
    description = models.CharField(max_length=250,default="")

class ProjectAdminMetadata(models.Model):
    project = models.OneToOneField(Project,on_delete=models.CASCADE,primary_key=True)
    owner = models.ForeignKey(User,models.DO_NOTHING,related_name="owner_projects")
    grant_access_users_pk = models.CharField(max_length=300,default="")
    grant_access_users_type = models.CharField(max_length=300,default="")

class GeoDataset(models.Model):
    id = models.BigAutoField(primary_key=True)
    string_id = models.CharField(max_length=150,unique=True)
    db_table = models.CharField(max_length=200)
    uploaded_by = models.ForeignKey(User, models.DO_NOTHING,related_name="geodatasets_uploads")


class GeoDatasetColumn(models.Model):
    id = models.BigAutoField(primary_key=True)
    geodataset = models.ForeignKey(GeoDataset,models.CASCADE,)
    name = models.CharField(max_length=100)
    alias = models.CharField(max_length=100)
    dtype = models.CharField(max_length=100)

