from django.urls import path
from . import views

app_name = 'restaurant'
urlpatterns = [
    path('', views.index, name='index'),
    path('booking/', views.BookingView.as_view(), name='booking'),
    path('menu/', views.MenuItemView.as_view(), name='menu'),
    path('menu/<int:pk>/', views.SingleMenuItemView.as_view(), name='single_menu'),
]