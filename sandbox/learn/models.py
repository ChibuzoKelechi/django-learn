import datetime
from django.db import models
from django.utils import timezone

# Create your models here.
class Question(models.Model):
    query_text = models.CharField(max_length=200)
    q_date = models.DateTimeField('Date Asked')
    
    def __str__(self):
        return f'{str(self.query_text)}'
    
    def asked_recent(self):
        return self.q_date >= timezone.now() - datetime.timedelta(days=1)
    

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete = models.CASCADE)
    choice_text = models.CharField(max_length = 200)
    votes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.choice_text