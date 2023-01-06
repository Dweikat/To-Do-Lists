# todo_list/todo_app/urls.py
# todo_list/todo_app/urls.py
from note import views
from django.urls import path,include
from note.views import ItemCreate

urlpatterns = [
    path("", views.ListListView.as_view(), name="index"),
path("list/<int:list_id>/", views.ItemListView.as_view(), name="list"),
# CRUD patterns for ToDoLists
path("list/add/", views.ListCreate.as_view(), name="list-add"),
# CRUD patterns for ToDoItems
path(
"list/<int:list_id>/item/add/",
views.ItemCreate.as_view(),
name="item-add",
),
path(
"list/<int:list_id>/item/<int:pk>/",
views.ItemUpdate.as_view(),
name="item-update",
),
]