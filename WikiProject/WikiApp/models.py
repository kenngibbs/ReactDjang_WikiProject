from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class MainWikiModel(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=2000)
    mainImage = models.ImageField(upload_to="WikiApp/", default="")
    userForeignKey = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)


class RelatedWikiModel(models.Model):
    title = models.CharField(max_length = 1000)
    relatedDescription = models.CharField(max_length = 1000)
    relatedImage = models.ImageField(upload_to="WikiApp/", default="")
    mainForeignKey = models.ForeignKey(MainWikiModel, on_delete=models.CASCADE, null=True, blank=True)
