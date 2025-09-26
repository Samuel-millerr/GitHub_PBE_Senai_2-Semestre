"""Views em Django são funções ou classes responsáveis por receber as requisições do usuário 
(como acessar uma página), processar a lógica necessária (como consultar o banco de dados) e 
retornar uma resposta, possívelmente em JSON.

Existem diversas formas de desenvolver esses metódos em Django, abaixo estão listadas
algumas formas de realizar esse processo.
"""

from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView
from rest_framework.decorators import api_view, permission_classes

from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.permissions import IsAuthenticated  

from models import Author
from serializers import AuthorSerializer

""" GENERICS """
# GET - Todos os autores
class AuthorsList(ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

# CREATE
class AuthorCreate(CreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

# GET
class AuthorList(RetrieveAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

# PUT
class AuthorUpdate(RetrieveUpdateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

# DELETE
class AuthorDelete(RetrieveDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


""" DECORATOR @api_view() """
# Criação do CRUD com o metódo api_view() - decorator
@api_view(['GET']) # Metódo GET para pegar todos os autores cadastrados
@permission_classes([IsAuthenticated])
def authors_list(request):
    filter_backends = [DjangoFilterBackend, SearchFilter]
    queryset = Author.objects.all()
    for filter in list(filter_backends):
        queryset = filter().filter_queryset(request, queryset, view=authors_list)
    serializer = AuthorSerializer(queryset, many=True)
    return Response(serializer.data)  

authors_list.filter_backends = [DjangoFilterBackend, SearchFilter]
authors_list.filterset_fields = ["nacionalidade", "data_nascimento"]
authors_list.search_fields = ["nome", "sobrenome"]

@api_view(['GET']) # Metódo GET para pegar um autor por ID
# @permission_classes([IsAuthenticated])
def author_list(request, pk):
    author = Author.objects.get(pk=pk)
    serializer = AuthorSerializer(author)
    return Response(serializer.data)

@api_view(['GET','POST']) # Metódo POST para criar um autor
@permission_classes([IsAuthenticated])
def author_create(request):
    if request.method == 'GET':
        author_model = Author.objects.model()
        serialiazer = AuthorSerializer(author_model)
        return Response(serialiazer.data)
    elif request.method == 'POST':
        serialiazer = AuthorSerializer(data = request.data)
        if serialiazer.is_valid():
            serialiazer.save()
            return Response(serialiazer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serialiazer.data, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET','PUT']) # Metódo PUT para atualizar um autor
# @permission_classes([IsAuthenticated])
def author_update(request, pk): 
    try: 
       author = Author.objects.get(pk=pk)
    except Author.DoesNotExist:
          return Response({"error": "Author not found"},status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = AuthorSerializer(author)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = AuthorSerializer(author, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else: 
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PATCH'])
# @permission_classes([IsAuthenticated])
def author_patch(request, pk):
    try:
        author = Author.objects.get(pk = pk)
    except: 
        return Response({"error","Author not found"}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = AuthorSerializer(author)
        return Response(serializer.data)
    elif request.method == 'PATCH':
        serializer = AuthorSerializer(author, data = request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
        
@api_view(['DELETE']) # Metódo DELETE para deletar um autor
# @permission_classes([IsAuthenticated])
def author_delete(request, pk): 
    try:
        author = Author.objects.get(pk=pk)
    except:
        return Response({"error": "Author not found"}, status=status.HTTP_400_BAD_REQUEST)

    author.delete()
    return Response({"message": "Author successfully delete"}, status=status.HTTP_200_OK)
