from django.db import models

class BaseModel(models.Model):
    abstract = True

    title = models.CharField(max_length=255, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


