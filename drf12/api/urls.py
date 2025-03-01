from django.urls import path
from api import views

urlpatterns = [
    # path('studentapi/', views.StudentList.as_view(), name='studentlist'),
    # path('studentapi/', views.StudentCreate.as_view(), name='studentlist'),
    # path('studentapi/<int:pk>', views.StudentRetrive.as_view(), name='studentlist'),
    # path('studentapi/<int:pk>', views.StudentUpdate.as_view(), name='studentlist'),
    # path('studentapi/<int:pk>', views.StudentDestroy.as_view(), name='studentlist'),
    path('studentapi/', views.StudentListCreate.as_view(), name='studentlist'),
    # path('studentapi/<int:pk>', views.StudentRetriveUpdate.as_view(), name='studentlist'),
    # path('studentapi/<int:pk>', views.StudentRetriveDestroy.as_view(), name='studentlist'),
    path('studentapi/<int:pk>', views.StudentRetriveUpdateDestroy.as_view(), name='studentlist'),



]
