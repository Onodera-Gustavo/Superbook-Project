from django.shortcuts import render
from django.views.generic import ListView
from .models import Post

# (FBV)
def lista_posts(request):
    posts = Post.objects.all()
    return render(request, "posts/lista_posts.html", {"posts": posts})

# CBV)
class ListaPostsView(ListView):
    model = Post
    template_name = "posts/lista_posts.html" 
    context_object_name = "posts"