from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from api.models import Livro
from api.serializers import BookSerializer

# GET - Pegar todos os livros
class BooksList(ListAPIView):
    queryset = Livro.objects.all()
    serializer_class= BookSerializer

# POST - Somente um livro
class BookCreate(CreateAPIView):
    queryset = Livro.objects.all()
    serializer_class = BookSerializer

# GET, PUT & DELETE - Somente um livro
class BookUpdateDelete(RetrieveUpdateDestroyAPIView):
    queryset = Livro.objects.all()
    serializer_class = BookSerializer