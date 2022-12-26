from django.contrib import admin
from django.urls import path, include
from store_api import views

urlpatterns = [
path('', views.home, name='home'),
path('store/', include('store_api.urls')),

    path('admin/', admin.site.urls),
]
