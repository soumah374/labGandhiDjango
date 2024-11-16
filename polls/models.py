from django.db import models

# Create your models here.

class Question(models.Model):
  question_text = models.CharField(max_length=255)
  pub_date = models.DateTimeField("date publication")

class Choice(models.Model):
  choice_text = models.CharField(max_length=255)
  question = models.ForeignKey(Question, on_delete=models.CASCADE)
  votes = models.IntegerField(default=0)
