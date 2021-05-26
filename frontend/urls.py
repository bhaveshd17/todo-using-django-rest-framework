from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
	path('', views.toDoList, name="toDoList"),
	path('create/', views.createList, name="create"),
	path('edit/<str:pk>', views.updateList, name="edit"),
	path('delete/<str:pk>', views.deleteList, name="delete"),
]