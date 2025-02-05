from api import views
from django.urls import path
# from api import views

urlpatterns = [
    path('', views.StudentAPI.as_view(), name='get_students')
]
