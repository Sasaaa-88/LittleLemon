from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    #path('menu_item/<int:pk>', views.display_menu_item, name='menu_item'),
]