from . import views
from django.urls import path

urlpatterns = [
    # path('students/', views.students, name='students')
    path('students/', views.StudentAPI.as_view(), name='students')
]
