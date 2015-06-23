from django.contrib import admin
from .models import CurrentTask, TaskType

class TaskAdmin(admin.ModelAdmin):
    search_fields = ['task']
    list_filter = ['task']
    list_display = ('task', 'frequency', 'date_due', )
#try adding person in charge later.. not sure if it's diff cuz foreign key

admin.site.register(CurrentTask, TaskAdmin)
admin.site.register(TaskType)