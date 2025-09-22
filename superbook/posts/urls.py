from django.urls import path
from . import views
from .views import (
    PostCreateView, PostListView, PostUpdateView, PostDeleteView, detalhe_post
)


app_name = 'posts'

urlpatterns = [
    path('lista/', PostListView.as_view(), name='lista_posts'),           # FBV
    path('cbv/', PostListView.as_view(), name='lista_posts_cbv'),  # CBV
    path('novo/', PostCreateView.as_view(), name='criar_post'),
    path('<int:pk>/editar/', PostUpdateView.as_view(), name='editar_post'),
    path('<int:pk>/excluir/', PostDeleteView.as_view(), name='excluir_post'),
    path('<int:pk>/', detalhe_post, name='detalhe_post'),  # detalhe por último

    
]

