from django.db import models
from questions.models import Question


# Create your models here.
class Answer(models.Model):
    answer_id = models.IntegerField(primary_key=True)
    text = models.TextField(null=True)
    upvote = models.IntegerField()
    downvote = models.IntegerField()
    question_id = models.ForeignKey(to=Question
    , on_delete='CASCADE')
