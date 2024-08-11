from django.urls import path
from . import views

urlpatterns = [
    path('', views.flashcard_list, name='flashcard_list'),
    path('<int:pk>/', views.flashcard_detail, name='flashcard_detail'),
    path('create/', views.flashcard_create, name='flashcard_create'),
    path('<int:pk>/edit/', views.flashcard_edit, name='flashcard_edit'),
    path('<int:pk>/delete/', views.flashcard_delete, name='flashcard_delete'),
]
