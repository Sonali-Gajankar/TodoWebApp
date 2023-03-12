import datetime

from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView, ListView, UpdateView, DetailView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from .models import TodoTasks
from .forms import TodoTaskForm


# Create your views here.
def home(request):
    return render(request, 'todo/home.html')

def about(request):
    return render(request, 'todo/about.html')


class CreateTaskView(LoginRequiredMixin, CreateView):
    template_name = "todo/task_create_form.html"
    model = TodoTasks
    form_class = TodoTaskForm

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
        date_filter = None
        day_range = self.kwargs.get('days')
        if day_range == 'today' or day_range is None:
            return TodoTasks.objects.filter(author=self.request.user,
                                            date_field=datetime.date.today())
        elif day_range == 'tomorrow':
            date_filter = datetime.datetime.now() + datetime.timedelta(1)
        elif day_range == 'next_seven_days':
            date_filter = datetime.datetime.now() + datetime.timedelta(7)
        elif day_range == 'month':
            date_filter = datetime.datetime.now() + datetime.timedelta(30)
        return TodoTasks.objects.filter(author=self.request.user,
                                        date_field__range=[datetime.datetime.now() + datetime.timedelta(1),
                                                           date_filter])  # date_field=datetime.date.today()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(TaskListView, self).get_context_data(**kwargs)
        day_range = self.kwargs.get('days')
        if day_range == 'today' or day_range is None:
            context['day'] = 'Today'
        elif day_range == 'tomorrow':
            context['day'] = 'Tomorrow'
        elif day_range == 'next_seven_days':
            context['day'] = 'Next Week'
        elif day_range == 'month':
            context['day'] = 'Next Month'

        context['top_five'] = TodoTasks.objects.filter(author=self.request.user).order_by('-date_field')[:5]
        context['starred_tasks'] = TodoTasks.objects.filter(author=self.request.user,starred=True,date_field__gte=datetime.datetime.now()).order_by('-date_field')[:5]
        return context


class TaskStatusUpdate(LoginRequiredMixin, View):
    template_name = "todo/user_tasks_add.html"
    form_class = TodoTaskForm

    def post(self, *args, **kwargs):
        task = TodoTasks.objects.get(pk=kwargs['pk'])
        if task.status == False:
            task.status = True
        else:
            task.status = False
        task.save()

        return HttpResponseRedirect(self.request.META.get('HTTP_REFERER', '/'))


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "todo/task_create_form.html"
    model = TodoTasks
    fields = ['title', 'description', 'category', 'date_field', 'starred']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(TaskUpdateView, self).form_valid(form)

    def test_func(self):
        entry = self.get_object()
        if entry.author == self.request.user:
            return True
        return False
