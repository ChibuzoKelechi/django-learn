from django.urls import path
from . import views

app_name = 'learn'
urlpatterns = [
     path("", views.index, name="index"),
     path('<int:question_id>/', views.questions, name="questions"),
     path('<int:question_id>/results/', views.results, name='results'),
     path('<int:question_id>/votes/', views.votes, name='votes'),
     path('<int:question_id>/details/', views.details, name='details'),
     path('blank/', views.blank, name='blank'),
]