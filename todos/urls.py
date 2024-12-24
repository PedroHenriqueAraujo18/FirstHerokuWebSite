from todos.views import (ListTodo, DetailTodo)
from django.urls import path

urlpatterns=[
    path("",ListTodo.as_view(),name='list_todo'),
    path("<int:pk>/",DetailTodo.as_view(),name='detail_todo'),
]