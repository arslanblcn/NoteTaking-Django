from django.contrib import admin

# Register your models here.
from .models import Task

class taskAdmin(admin.ModelAdmin):
    list_display = ['id', 'taskTitle']
    search_fields = ['taskTitle', 'taskContent']
admin.site.register(Task, taskAdmin)