from django.contrib import admin

# Register your models here.
from api.models import Student

class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'roll', 'city']

admin.site.register(Student, StudentAdmin)