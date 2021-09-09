from django.shortcuts import (
    get_object_or_404,
    render,
    HttpResponseRedirect,
)
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.edit import UpdateView
from .models import Task
from .forms import updateForm
# Create your views here.

class TaskUpdateView( UpdateView):
    model = Task
    template_name = "tasks/update.html"
    form_class = updateForm
    success_url = "/home/"
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(TaskUpdateView, self).dispatch(*args, **kwargs)


@login_required(login_url="/")
def task_detail_view(request, id = None):
    task_obj = None
    if id is not None:
        task_obj = Task.objects.get(id = id)
    context = {
        "object" : task_obj,
    }
    return render(request, "tasks/detail.html", context=context)

@login_required(login_url="/")
def task_create_view(request):
    context = {}
    if request.method == "POST":
        title = request.POST.get("task_title")
        content = request.POST.get("task_content")
        task_object = Task.objects.create(taskTitle=title, taskContent=content)
        context['object'] = task_object
        context['created'] = True
    
    return render(request, "tasks/create.html", context=context)

@login_required(login_url="/")
def task_search_view(request):
    query_dict = request.GET
    # query = query_dict.get("q") # search form query
    try: 
        query = query_dict.get("q")
    except:
        query = None
    task_obj = None
    if query is not None:
        task_obj = Task.objects.filter(taskTitle__icontains = query)
    context = {
        "object" : task_obj,
    }
    return render(request, "tasks/search.html", context=context)

@login_required(login_url="/")
def task_delete_view(request, id):
    context = {}
    obj = get_object_or_404(Task, id = id)
    context["object"] = obj
    context["deleted"] = False
    if request.method == "POST":
        obj.delete()
        return HttpResponseRedirect("/home/")
    return render(request, "tasks/delete.html", context=context)

def handler404(request, exception, template_name="404.html"):
    
    return render(request, template_name, {})

def handler500(request, *args, **argv):
    return render(request, '500.html', status=500)