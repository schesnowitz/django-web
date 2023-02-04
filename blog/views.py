from django.shortcuts import render
# from django.http import HttpResponse
# for class based views... 
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView, 
    UpdateView, 
    DeleteView
    )
from django.urls import reverse_lazy
from.models import Post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


# def home(request):

#     context = {
#         'posts' : Post.objects.all()
#     }
#     return render(request, 'blog/home.html', context) 

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html' # TemplateDoesNotExist at / blog/post_list.html
    context_object_name = 'posts' # setting name for view as 
    # otherwise looks for the default which is object list
    ordering = ['-date_posted'] # (variable) ordering: list[str]

class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user 
        return super().form_valid(form)
    # success_url = reverse_lazy('blog-home')
''' post created but error -> No URL to redirect to.  
Either provide a url or define a get_absolute_url method on the Model. 
this is set in the model get_absolute_url to redirect to home, for example use success url'''
class PostUpdateView(UserPassesTestMixin, LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user 
        return super().form_valid(form)
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False 
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

def about(request):
    return render(request, 'blog/about.html') 



