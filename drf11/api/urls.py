from api import views
from django.urls import path

urlpatterns = [
    path('studentapi/', views.StudentList.as_view(), name = 'studentlist'),
    # path('studentapi/', views.StudentCreate.as_view(), name = 'studentcreate'),
    # path('studentapi/<int:pk>', views.StudentRetrive.as_view(), name = 'studentretrive'),
    # path('studentapi/<int:pk>', views.StudentUpdate.as_view(), name = 'studentupdate'),
    path('studentapi/<int:pk>', views.StudentDestroy.as_view(), name = 'studentdestroy'),
]
