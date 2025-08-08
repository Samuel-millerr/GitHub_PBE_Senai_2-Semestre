from rest_framework.generics import  ListAPIView, CreateAPIView, RetrieveAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView
from api.models import Autor
from api.serializers import AuthorSerializer

# GET - Todos os autores
class AuthorsList(ListAPIView):
    queryset = Autor.objects.all()
    serializer_class = AuthorSerializer

# CREATE
class AuthorCreate(CreateAPIView):
    queryset = Autor.objects.all()
    serializer_class = AuthorSerializer

# GET
class AuthorList(RetrieveAPIView):
    queryset = Autor.objects.all()
    serializer_class = AuthorSerializer

class AuthorUpdate(RetrieveUpdateAPIView):
    queryset = Autor.objects.all()
    serializer_class = AuthorSerializer

class AuthorDelete(RetrieveDestroyAPIView):
    queryset = Autor.objects.all()
    serializer_class = AuthorSerializer



