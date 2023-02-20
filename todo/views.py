import datetime

from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView, UpdateView, DetailView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import TodoTasks
from .forms import TodoTaskForm


# Create your views here.
def home(request):
    return render(request, 'todo/home.html')


class CreateTaskView(LoginRequiredMixin, CreateView):
    template_name = "todo/task_create_form.html"
    model = TodoTasks
    fields = ['title', 'description', 'starred', 'category']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class TaskListView(LoginRequiredMixin, ListView):
    template_name = "todo/user_tasks_add.html"
    context_object_name = "user_tasks"
    paginate_by = 5

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(TaskListView, self).form_valid(form)

    def get_queryset(self):
        return TodoTasks.objects.filter(author=self.request.user)  # date_field=datetime.date.today()


class TaskStatusUpdate(LoginRequiredMixin, View):
    template_name = "todo/user_tasks_add.html"
    form_class = TodoTaskForm

    def get_object(self):
        obj = super().get_object()
        obj.status = True
        obj.save()
        return redirect('task-list')

    def post(self, *args, **kwargs):
        task = TodoTasks.objects.get(pk=kwargs['pk'])
        if task.status == False:
            task.status = True
        else:
            task.status = False
        task.save()

        return redirect("task-list")
