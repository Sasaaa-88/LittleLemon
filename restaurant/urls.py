from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('items/', views.MenuItemsView.as_view()),
    path('item/<int:pk>', views.SingleMenuItemView.as_view()),
]