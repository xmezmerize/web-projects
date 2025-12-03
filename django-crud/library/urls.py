from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list, name='book_list'),           # listar
    path('add/', views.book_create, name='book_create'),   # criar
    path('edit/<int:pk>/', views.book_update, name='book_update'), # atualizar
    path('delete/<int:pk>/', views.book_delete, name='book_delete'), # deletar
]