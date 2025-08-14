from django.urls import path
from .views.viewAuthors import *
from .views.viewBooks import *

urlpatterns = [
    path('viewAllAuthors/', authors_list),
    path('viewCreateAuthor/', author_create),
    path('viewListAuthor/<int:pk>', author_list),
    path('viewUpdateAuthor/<int:pk>', author_update),
    path('viewDeleteAuthor/<int:pk>', author_delete),
    path('viewListBooks/', BooksList.as_view()),
    path('viewCreateBook/', BookCreate.as_view()),
    path('viewUpdateDeleteBook/<int:pk>', BookUpdateDelete.as_view())
]