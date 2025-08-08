from rest_framework import serializers
from .models import Autor,Livro

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Livro
        fields = '__all__'
