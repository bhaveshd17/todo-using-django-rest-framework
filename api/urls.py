from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
	path('', views.apiOverview, name="apiOverview"),
	path('task-list/', views.taskList, name="task-list"),
	path('task-details/<str:pk>/', views.taskView, name="task-details"),
	path('task-create/', views.taskCreate, name="task-create"),
	path('task-update/<str:pk>/', views.taskUpdate, name="task-update"),
	path('task-delete/<str:pk>/', views.taskDelete, name="task-delete"),
]