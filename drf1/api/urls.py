from django.urls import path
from . import views

urlpatterns = [
    path('student/<int:id>', views.student_details, name='student_details'),
    path('student', views.student_details_all, name='student_details'),


]
