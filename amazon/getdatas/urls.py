from django.urls import path 
from . import views
##url kaydetme (uygulama için)
urlpatterns = [
    path("" , views.home , name="home")
]