from django.core.paginator import  Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from tasks.models import Task

@login_required(login_url="/")
def index_view(request, *args, **kwargs):
    #data = Task.objects.get(id = 1)
    tasks_list = Task.objects.all()
    pagination = Paginator(tasks_list, 3)
    page_number = request.GET.get('page')
    page_obj =  pagination.get_page(page_number)
    context = {
        #"list" : tasks_list,
        "records" : tasks_list.count(),
        "page_obj" : page_obj,
        #"obj" : data,
        #"title" : data.taskTitle,
        #"content" : data.taskContent,
        #"id" : data.id,
    }

    return render(request, "home-view.html", context=context)
    
