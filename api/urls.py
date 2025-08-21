from django.urls import path
from .views.viewAuthors import *
from .views.viewBooks import *
from .views.viewPublishers import *

urlpatterns = [
    # URLS DOS AUTORES
    path('viewAllAuthors/', authors_list),
    path('viewCreateAuthor/', author_create),
    path('viewListAuthor/<int:pk>', author_list),
    path('viewUpdateAuthor/<int:pk>', author_update),
    path('viewDeleteAuthor/<int:pk>', author_delete),
    # URLS DAS EDITORAS
    path('viewAllPublishers/', publishers_list),
    path("viewCreatePublisher/", publisher_create),
    #URLS DOS LIVROS
    path('viewAllBooks/', BooksList.as_view()),
    path('viewCreateBook/', BookCreate.as_view()),
    path('viewUpdateDeleteBook/<int:pk>', BookUpdateDelete.as_view())
]