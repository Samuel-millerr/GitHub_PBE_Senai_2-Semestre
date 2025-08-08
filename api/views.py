# As views são utilizadas para a aplicação das regras de negócio dentro do projeto
from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
from .models import Autor, Livro
from .serializers import AuthorSerializer, BookSerializer

# Criação do CRUD de autores
class AutorListCreate(ListCreateAPIView):
    queryset = Autor.objects.all()  
    serializer_class = AuthorSerializer

class AutoresListView(ListAPIView):
    queryset = Autor.objects.all()
    serializer_class = AuthorSerializer

class AutorDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = Autor.objects.all()
    serializer_class = AuthorSerializer

# Criação de CRUD de livros
class BookListCreate(ListCreateAPIView):
    queryset = Livro.objects.all()
    serializer_class = BookSerializer

class BookListView(ListAPIView):
    queryset = Livro.objects.all()
    serializer_class = BookSerializer

class BookDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = Livro.objects.all()
    serializer_class = BookSerializer
