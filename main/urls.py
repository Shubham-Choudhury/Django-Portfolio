from django.urls import path, include

from main import views

urlpatterns = [
    path('', views.index, name='home'),
    # path('projects/', views.projects),
    
]