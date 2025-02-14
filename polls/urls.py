from django.urls import path
from . import views

app_name = 'polls'
urlpatterns = [
  path("",views.IndexView.as_view(), name="index"),
  path("details/<int:pk>", views.DetailView.as_view(), name="details"),
  path("add", views.QuestionView.as_view(), name="add"),
]