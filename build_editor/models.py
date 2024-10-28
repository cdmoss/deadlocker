from django.db import models
from django.core.validators import validate_comma_separated_integer_list

class LocalDeadlockBuild(models.Model):
    id = models.UUIDField(primary_key=True)
    hero_id = models.IntegerField()
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    name = models.CharField(max_length=255)
    description = models.TextField()

class LocalDeadlockBuildCategory(models.Model):
    id = models.UUIDField(primary_key=True)
    build = models.ForeignKey(LocalDeadlockBuild, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    item_ids = models.CharField(max_length=255, validators=[validate_comma_separated_integer_list])

