from django.urls import path
from .views.viewAuthors import *

urlpatterns = [
    path('viewAllAuthors/', AuthorsList.as_view()),
    path('viewCreateAuthor/', AuthorCreate.as_view()),
    path('viewListAuthor/<int:pk>', AuthorList.as_view()),
    path('viewUpdateAuthor/<int:pk>', AuthorUpdate.as_view()),
    path('viewDeleteAuthor/<int:pk>', AuthorDelete.as_view())
]