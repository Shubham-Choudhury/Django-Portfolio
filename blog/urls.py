from django.urls import path, include

from blog import views

urlpatterns = [
    path('', views.index),
    path('single-blog/', views.blog),
    
]