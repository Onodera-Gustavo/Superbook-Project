from django.urls import path
from . import views
from .views import HeroListView

urlpatterns = [
    path('hello/', views.hello_heroes, name='hello_heroes'),
    path('lista/', views.lista_herois, name='lista_herois'),
    path('cbv-lista/', HeroListView.as_view(), name='cbv_lista_herois'),
    path('novo/', views.criar_heroi, name='criar_heroi'),

]