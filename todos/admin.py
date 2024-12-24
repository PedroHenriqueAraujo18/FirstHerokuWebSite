from django.contrib import admin
from todos.models import Todo
# Register your models here.

class AdminTodos(admin.ModelAdmin):
    list_display=[
        "title",
        "body"
    ]

admin.site.register(Todo, AdminTodos)