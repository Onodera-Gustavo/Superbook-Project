from django.urls import path
from . import views

urlpatterns = [
    path('lista/', views.lista_posts, name='lista_posts'),                 # FBV
    path('cbv/', views.ListaPostsView.as_view(), name='lista_posts_cbv'),  # CBV
    path('novo/', views.criar_post, name='criar_post'),
]