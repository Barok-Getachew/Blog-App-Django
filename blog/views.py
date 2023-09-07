from django.shortcuts import render
from django.views import generic
from .models import blog
from django.urls import  reverse_lazy
# Create your views here.
class BlogListView(generic.ListView):
    model = blog
    template_name  = 'home.html'
class BlogDetailView(generic.DetailView):
    model = blog
    template_name = 'detail.html'

class BlogCreateView(generic.CreateView):
    model = blog
    template_name = 'new.html'
    fields = ['title','body','author']
class BloUpdateView(generic.UpdateView):
    model = blog
    template_name = 'edit.html'
    fields = ['title','body']
class DeleteView(generic.DeleteView):
    model = blog
    template_name = 'delete.html'
    success_url = reverse_lazy('home')