from django.urls import path
from .views.viewAuthors import *
from .views.viewBooks import *
from .views.viewPublishers import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    # URLS DOS AUTORES
    path('viewAllAuthors/', authors_list),
    path('viewCreateAuthor/', author_create),
    path('viewCreateAuthorCsv/', author_create_csv),
    path('viewListAuthor/<int:pk>', author_list),
    path('viewUpdateAuthor/<int:pk>', author_update),
    path('viewUpdatePartialAuthor/<int:pk>', author_patch),
    path('viewDeleteAuthor/<int:pk>', author_delete),
    # URLS DAS EDITORAS
    path('viewAllPublishers/', PublisherView.as_view()),
    path('viewPublishers/<int:pk>', PublisherView.as_view()),
    #URLS DOS LIVROS
    path('viewAllBooks/', books_list),
    path('viewListBook/', book_list),
    path('viewCreateBook/', book_create),
    path('viewUpdateBook/', book_update),
    path('viewUpdatePartialBook/', book_patch),
    path('viewDeleteBook/', book_delete),   
    #JWT
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh')
]