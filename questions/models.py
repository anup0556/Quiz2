from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    options = models.JSONField(default=dict)
    correct_answer = models.CharField(max_length=200)

    def __str__(self):
        return self.question_text
