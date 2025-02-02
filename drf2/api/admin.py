from django.contrib import admin

# Register your models here.
from api.models import Student

class StundetAdmin(admin.ModelAdmin):
    list_display = ['name', 'roll', 'city']

admin.site.register(Student, StundetAdmin)
