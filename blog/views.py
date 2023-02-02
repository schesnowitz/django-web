from django.shortcuts import render
# from django.http import HttpResponse
from.models import Post

# posts = [
#     {
#         'author' : 'Hank Smith',
#         'title' : "Post 1",
#         'content' : 'post 1 content',
#         'date_posted ': 'August 1, 2025',  
#     },
#     {
#         'author' : 'Steve o',
#         'title' : "Post 2",
#         'content' : 'post 2 content content really coming out of this file',
#         'date_posted ': 'August 2, 2025',  
#     }
# ]



def home(request):

    context = {
        'posts' : Post.objects.all()
    }
    return render(request, 'blog/home.html', context) 

def about(request):
    return render(request, 'blog/about.html') 

