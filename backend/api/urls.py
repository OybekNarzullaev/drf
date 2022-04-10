from django.urls import path
from . import views

urlpatterns = [
    path('', views.api_home),
    path('post/', views.post_data)
]