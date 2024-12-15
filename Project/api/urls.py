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