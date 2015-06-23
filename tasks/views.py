from django.shortcuts import render
from django.http import HttpResponse
from .models import CurrentTask
from django.template import Context, loader

def index(request):
    task_list = CurrentTask.objects.all()
    t = loader.get_template('tasks/index.html')
    c = Context('task_list', task_list)
    return HttpResponse(t.render(c))
