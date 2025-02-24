from api import views
from django.urls import path

urlpatterns = [
    path('studentapi/', views.StudentAPI.as_view(), name='studentapi')
]
