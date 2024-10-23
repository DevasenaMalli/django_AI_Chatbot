from django.db import models

# Create your models here.
class Past(models.Model):
    question = models.CharField(max_length=100)
    answer = models.TextField(max_length=300)


    def __str__(self):
        return self.question
