from django.contrib import admin

# Register your models here.
from . models import Student

class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'roll', 'city']

admin.site.register(Student, StudentAdmin)