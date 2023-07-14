import imp
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('login/', views.loginPage, name="login"),
    path('register/', views.registerUser, name="register"),
    path('logout/', views.logoutUser, name="logout"),
    path('room/<str:pk>/', views.room, name="room"),
    path('create-room/', views.createRoom, name="create-room"),
    path('edit-user/', views.updateUser, name="edit-user"),
    path('user-profile/<str:pk>/', views.profilePage, name="user-profile"),
    path('update-room/<str:pk>/', views.updateRoom, name="update-room"),
    path('delete-room/<str:pk>/', views.deleteRoom, name="delete-room"),
    path('delete-message/<str:pk>/', views.deleteMessage, name="delete-message"),
]
