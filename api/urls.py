from django.urls import path
from .views.viewAuthors import *
from .views.viewBooks import *

urlpatterns = [
    path('viewAllAuthors/', AuthorsList.as_view()),
    path('viewCreateAuthor/', AuthorCreate.as_view()),
    path('viewListAuthor/<int:pk>', AuthorList.as_view()),
    path('viewUpdateAuthor/<int:pk>', AuthorUpdate.as_view()),
    path('viewDeleteAuthor/<int:pk>', AuthorDelete.as_view()),
    path('viewListBook/', BooksList.as_view()),
    path('viewCreateBook/', BookCreate.as_view()),
    path('viewUpdateDeleteBook/<int:pk>', BookUpdateDelete.as_view())
]