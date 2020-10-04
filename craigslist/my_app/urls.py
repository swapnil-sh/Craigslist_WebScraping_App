from django.urls import path
from django.contrib import admin
from . import views
from my_app import views

urlpatterns = [
    path('',views.home,name='home'),
    #path('admin/', admin.site.urls),
] 