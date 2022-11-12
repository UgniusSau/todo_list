from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from .models import Task
from .forms import CreateForm


class CustomLoginView(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('tasks')

class RegisterPage(FormView):
    template_name = 'base/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)
    
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('tasks')
        return super(RegisterPage, self).get(*args, **kwargs)




class TaskList(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'tasks'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        context['count'] = context['tasks'].filter(complete=False).count()
        return context

class TaskDetail(LoginRequiredMixin, DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'base/task.html'

# class TaskCreate(LoginRequiredMixin, CreateView):
#     model = Task
#     fields = ['title', 'start_date', 'end_date', 'complete']

#     success_url = reverse_lazy('tasks')
#     form = ExampleForm()
#     def form_valid(self, form):
#         form.instance.user = self.request.user
#         return super(TaskCreate, self).form_valid(form)

def CreateTask(request):
    form = CreateForm()
    if request.method == 'POST':
        form = CreateForm(request.POST)
        form.instance.user = request.user
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'base/task_form.html', context)

# class TaskUpdate(LoginRequiredMixin, UpdateView):
#     model = Task
#     fields = ['title', 'start_date', 'start_date_time', 'end_date','end_date_time', 'complete']
#     success_url = reverse_lazy('tasks')

def UpdateTask(request, pk):
    task = Task.objects.get(id=pk)
    form = CreateForm(instance=task)

    if request.method == 'POST':
        form = CreateForm(request.POST, instance=task)
        form.instance.user = request.user
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form':form}
    return render(request, 'base/task_form.html', context)

class DeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')
