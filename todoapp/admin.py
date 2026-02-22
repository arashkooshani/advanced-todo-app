from django.contrib import admin

from .models import Task,Category

class TaskAdmin(admin.ModelAdmin):
    list_display = ('creator','title','completed')

admin.site.register(Task,TaskAdmin)
admin.site.register(Category)
