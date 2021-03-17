from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('create/', views.create, name='entry-create'),
    path('master/', views.master, name='master'),
    path('mypasswords/', views.showpasswords, name='mypasswords'),
    path('', views.home, name='passwords-home'),
    path('entry/<int:pk>/delete/', views.delete, name='entry-delete'),
]
