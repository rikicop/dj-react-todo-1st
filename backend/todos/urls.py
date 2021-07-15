# todos/urls.py
from django.urls import path
from .views import ListTodo, DetailTodo, ListConstante

urlpatterns = [
    path('<int:pk>/', DetailTodo.as_view()),
    path('', ListTodo.as_view()),
    path('const', ListConstante.as_view()),
]
