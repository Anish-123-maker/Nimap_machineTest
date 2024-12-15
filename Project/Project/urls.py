"""
URL configuration for Project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from api.views import RegisterClientView,FetchClientsView,EditDeleteClientView,AddUserView,AddProjectView,UpdateUserView,UserProjectsView
urlpatterns = [
    path('register-client/', RegisterClientView.as_view(), name='register-client'),
    path('fetch-clients/', FetchClientsView.as_view(), name='fetch-clients'),
    path('edit-client/<int:pk>/', EditDeleteClientView.as_view(), name='edit-client'),
    path('delete-client/<int:pk>/', EditDeleteClientView.as_view(), name='delete-client'),
     path('add-user/', AddUserView.as_view(), name='add-user'),
    path('update-user/<int:pk>/', UpdateUserView.as_view(), name='update-user'),
    path('add-project/', AddProjectView.as_view(), name='add-project'),
    path('user-projects/<int:user_id>/', UserProjectsView.as_view(), name='user-projects'),
    
]
