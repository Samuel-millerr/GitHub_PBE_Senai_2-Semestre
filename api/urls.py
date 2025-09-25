from django.urls import path
from .views.viewAuthors import AuthorView
from .views.viewBooks import BookView
from .views.viewPublishers import PublisherView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    # URLS DOS AUTORES
    path('viewAuthor/', AuthorView.as_view()),
    path('viewAuthor/<int:pk>', AuthorView.as_view()),
    # URLS DAS EDITORAS
    path('viewPublisher/', PublisherView.as_view()),
    path('viewPublisher/<int:pk>', PublisherView.as_view()),
    #URLS DOS LIVROS
    path('viewBook/', BookView.as_view()),
    path('viewBook/<int:pk>', BookView.as_view()),
    #JWT
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh')
]