# As views são utilizadas para a aplicação das regras de negócio dentro do projeto
from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
from .models import Autor
from .serializers import AutorSerializer

class AutorListCreate(ListCreateAPIView):
    queryset = Autor.objects.all()  
    serializer_class = AutorSerializer

class AutoresListView(ListAPIView):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer

class AutorDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
