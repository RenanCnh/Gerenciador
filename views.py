from .models import todo
from django.views.generic import ListView, CreateView, UpdateView,DeleteView,View
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404,redirect
from datetime import date

class TodoListView(ListView):
    model = todo

class TodoCreateView(CreateView):
    model = todo    
    fields = ["title", "deadline"]
    success_url = reverse_lazy("todo_list")

class TodoUpdateView(UpdateView):
    model = todo
    fields = ["title", "deadline"]
    success_url = reverse_lazy("todo_list")

class TodoDeleteView(DeleteView):
    model = todo    
    success_url = reverse_lazy("todo_list")

class TodoCompleteView(View):
    def get(self, request , pk):   
            Todo = get_object_or_404(todo, pk=pk)
            Todo.mark_has_complete()
            return redirect("todo_list")