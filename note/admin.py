from django.contrib import admin

# todo_list/todo_app/admin.py
from django.contrib import admin
from note.models import ToDoItem, ToDoList
admin.site.register(ToDoItem)
admin.site.register(ToDoList)
