from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from .models import Post
from .forms import PostForm

# --- CBVs CRUD de Posts ---
class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'posts/form_post.html'
    success_url = reverse_lazy('lista_posts')

class PostListView(ListView):
    model = Post
    template_name = 'posts/lista_posts.html'
    context_object_name = 'posts'
    paginate_by = 12  # opcional

class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'posts/form_post.html'
    success_url = reverse_lazy('posts:lista_posts')

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'posts/confirmar_exclusao.html'
    success_url = reverse_lazy('posts:lista_posts') 


# --- FBV: detalhe do post + criação de comentário (comments app) ---
from comments.forms import ComentarioForm  # import do app comments
def detalhe_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    # comentários relacionados via related_name='comentarios'
    comentarios = post.comentarios.all().order_by('criado_em')

    if request.method == "POST":
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.post = post
            comentario.save()
            return redirect('posts:detalhe_post', pk=post.pk)
    else:
        form = ComentarioForm()

    return render(request, 'posts/detalhe_post.html', {
        'post': post,
        'comentarios': comentarios,
        'form': form,
    })
