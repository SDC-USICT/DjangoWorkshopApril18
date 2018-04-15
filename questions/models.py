from django.db import models

# Create your models here.
class Question(models.Model):
    text = models.TextField()
    upvotes = models.IntegerField(null=True)
    downvotes = models.IntegerField()
