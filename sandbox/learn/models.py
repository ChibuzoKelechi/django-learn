import datetime
from django.db import models
from django.utils import timezone
from django.contrib import admin

# Create your models here.
class Question(models.Model):
    query_text = models.CharField(max_length=200)
    q_date = models.DateTimeField('Date Asked')
    
    def __str__(self):
        return self.query_text 
    
    @admin.display(
        boolean=True, 
        ordering='q_date',
        description='Published recently?'
    )
    
    def asked_recent(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.q_date <= now
    
 
class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete = models.CASCADE)
    choice_text = models.CharField(max_length = 200)
    votes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.choice_text