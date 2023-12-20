from django.test import TestCase
import datetime
from django.utils import timezone

from .models import Question


# Create your tests here.
class QuestionModelTests(TestCase):
    def test_was_published_recently_with_future_question(self):
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(q_date=time)
        self.assertIs(future_question.asked_recent(), True)