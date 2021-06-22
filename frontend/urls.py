from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
	path('index/', views.toDoList, name="toDoList"),
	path('create/', views.createList, name="create"),
	path('edit/<str:pk>', views.updateList, name="edit"),
	path('delete/<str:pk>', views.deleteList, name="delete"),
	path('', views.loginUser, name='loginUser'),
	path('signinUser/', views.signInUser, name='signInUser'),
	path('logout/', views.logoutUser, name='logout'),
	path('view/', views.view_api, name='view')
]