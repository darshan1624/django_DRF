from api import views
from django.urls import path

urlpatterns = [
    path('', views.get_students, name='get_students')
]
