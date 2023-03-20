from generator import views
from django.contrib import admin
from django.urls import path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('password', views.password, name='password'),
    path('about', views.about, name='about')
]
