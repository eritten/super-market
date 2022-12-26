from django.urls import path
from . import views
urlpatterns = [
    path('signup/', views.create_user, name="create_user"),
    path('create-store/', views.create_store, name='create_store'),
path('login/', views.login_user, name='login_user'),
]
