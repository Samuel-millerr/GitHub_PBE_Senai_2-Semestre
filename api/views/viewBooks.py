from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from api.models import Livro
from api.serializers import BookSerializer

class BooksList(ListAPIView):
    queryset = Livro.objects.all()
    serializer_class= BookSerializer

class BookCreate(CreateAPIView):
    queryset = Livro.objects.all()
    serializer_class = BookSerializer

class BookUpdateDelete(RetrieveUpdateDestroyAPIView):
    queryset = Livro.objects.all()
    serializer_class = BookSerializer