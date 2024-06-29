from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('submit/', views.climate_submit, name='climate_submit'),
    path('submit/<int:climate_id>/', views.climate_submit, name='climate_submit_with_id'),
    path('base/', views.base_view, name='base'),
]