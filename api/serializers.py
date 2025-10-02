from rest_framework import serializers
from .models import Author, Book, Publisher

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class PublisherSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Publisher
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    autor = AuthorSerializer(read_only=True)
    editora = PublisherSerializer(read_only=True)
    class Meta:
        model = Book
        fields = ['titulo', 'subtitulo', 
                  'autor', 'editora', 
                  'isbn', 'descricao', 
                  'idioma', 'ano_publicacao', 
                  'paginas', 'preco', 
                  'estoque', 'desconto', 
                  'disponivel', 'dimensoes', 'peso']