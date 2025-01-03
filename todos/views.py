from rest_framework import generics
from todos.models import Todo
from todos.serializers import TodoSerializer

class ListTodo(generics.ListAPIView):
    queryset=Todo.objects.all()
    serializer_class=TodoSerializer

class DetailTodo(generics.RetrieveAPIView):
    queryset=Todo.objects.all()
    serializer_class = TodoSerializer

# Create your views here.
