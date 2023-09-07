from django.urls import path
from .views import BlogListView,BlogDetailView,BlogCreateView,BloUpdateView,DeleteView

urlpatterns = [
   path( '',BlogListView.as_view(), name='home'),
   path('post/<int:pk>',BlogDetailView.as_view(), name = 'detail_view'),
   path('post/new',BlogCreateView.as_view(),name = 'createBlog'),
   path('post/<int:pk>/edit',BloUpdateView.as_view() , name= 'edit'),
   path('post/<int:pk>/delete',DeleteView.as_view(), name = 'delete')
]