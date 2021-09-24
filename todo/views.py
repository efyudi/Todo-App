from django.shortcuts import render, reverse
from django.http import JsonResponse
from django.views.generic import CreateView, UpdateView, ListView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from .models import TodoModel

class TodoListView(LoginRequiredMixin, ListView):
    model = TodoModel
    template_name = 'todo/todo_list_view.html'

    def get_context_data(self, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['additional_text'] = "- Tasks"
        return context
    
    def get_queryset(self):
        return TodoModel.objects.filter(user=self.request.user)
    
    def get_login_url(self):
        return reverse("user_login")

class AddTaskCreateView(LoginRequiredMixin, CreateView):
    model = TodoModel
    fields = ['name']
    template_name = 'todo/add_task_create.html'

    def get_context_data(self, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['additional_text'] = "- Add Task"
        return context
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    def get_login_url(self):
        return reverse("user_login")


class DeleteTask(LoginRequiredMixin, DeleteView):
    model = TodoModel
    template_name = 'todo/delete_task.html'
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse("todo_home")
        

@login_required
def update_task(request, **kwargs):
    if request.GET.get('option'):
        obj = TodoModel.objects.get(pk=int(kwargs.get('pk')))
        obj.option = 'true' == request.GET['option']
        obj.save()

    return JsonResponse()
