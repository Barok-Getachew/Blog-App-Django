from django.shortcuts import render
from django.views import generic
from .models import blog
# Create your views here.
class BlogListView(generic.ListView):
    model = blog
    template_name  = 'home.html'
class BlogDetailView(generic.DetailView):
    model = blog
    template_name = 'detail.html'