from django.urls import path
from .views import *

urlpatterns = [
    path('createAuthor/', AutorListCreate.as_view()),
    path('viewAuthors/', AutoresListView.as_view()),
    path('deleteAuthor/<int:pk>', AutorDeleteView.as_view()),
    path('createBook/', BookListCreate.as_view()),
    path('viewBooks/', BookListView.as_view()),
    path('deleteBook/<int:pk>', BookDeleteView.as_view())
]