from django.urls import path
from .import views
urlpatterns = [
    path('', views.home, name = 'home'),
    path('cattleya/', views.cattleya, name ='cattleya'),
    path('dendrobium/', views.dendrobium, name = 'dendrobium')

]