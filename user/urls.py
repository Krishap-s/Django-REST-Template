from django.urls import path
from user import views

urlpatterns= [
    path(r"users/me",views.CurrentUser.as_view(),name='users-me')
    ]