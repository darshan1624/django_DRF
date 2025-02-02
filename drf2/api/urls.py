from . import views
from django.urls import path 

urlpatterns = [
    path('', views.student_create, name='student_create')
]