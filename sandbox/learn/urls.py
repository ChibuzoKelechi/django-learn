from django.urls import path
from . import views

app_name = 'learn'
urlpatterns = [
     path("", views.IndexView.as_view(), name="index"),
     path('<int:pk>/', views.DetailView.as_view(), name='details'),
     path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
     path("<int:question_id>/votes/", views.votes, name="votes"),
     # path('<int:pk>/', views.QuestionsView.as_view(), name="questions"),
     path('blank/', views.blank, name='blank'),
]