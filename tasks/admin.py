from django.contrib import admin
from .models import Task
# Register your models here.
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_completed')
    list_filter = ('is_completed',)
    search_fields = ('title',)

# Register the Task model using the TaskAdmin custom admin class
admin.site.register(Task, TaskAdmin)