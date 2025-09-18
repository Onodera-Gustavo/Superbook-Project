from django.shortcuts import render
from django.views.generic import ListView
from .models import Post
from django.shortcuts import render, redirect
# Ensure that 'forms.py' exists in the same directory as this file.
from .forms import PostForm
# (FBV)
def lista_posts(request):
    posts = Post.objects.all()
    return render(request, "posts/lista_posts.html", {"posts": posts})

# CBV)
class ListaPostsView(ListView):
    model = Post
    template_name = "posts/lista_posts.html" 
    context_object_name = "posts"


def criar_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_posts')
    else:
        form = PostForm()
    return render(request, "posts/form_post.html", {"form": form})