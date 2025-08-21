from rest_framework import status

from rest_framework.generics import  ListAPIView, CreateAPIView, RetrieveAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView

from rest_framework.response import Response

from rest_framework.decorators import api_view

from api.models import Author
from api.serializers import AuthorSerializer

"""# Criação do CRUD com o metódo generics
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

# PUT
class AuthorUpdate(RetrieveUpdateAPIView):
    queryset = Autor.objects.all()
    serializer_class = AuthorSerializer

DELETE
class AuthorDelete(RetrieveDestroyAPIView):
    queryset = Autor.objects.all()
    serializer_class = AuthorSerializer"""

# Criação do CRUD com o metódo api_view() - decorator
@api_view(['GET'])
def authors_list(request):
    queryset = Author.objects.all()
    serializer = AuthorSerializer(queryset, many=True)
    return Response(serializer.data)  
    
@api_view(['GET'])
def author_list(request, pk):
    autor = Author.objects.get(pk=pk)
    serializer = AuthorSerializer(autor)
    return Response(serializer.data)

@api_view(['POST'])
def author_create(request):
    serialiazer = AuthorSerializer(data = request.data)
    if serialiazer.is_valid():
        serialiazer.save()
        return Response(serialiazer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serialiazer.data, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['PUT'])
def author_update(request, pk):
    try: 
       autor = Author.objects.get(pk=pk)
    except Author.DoesNotExist:
          return Response({"error": "Item not found"},status=status.HTTP_404_NOT_FOUND)
    
    serializer = AuthorSerializer(autor, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else: 
        return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])  
def author_delete(request, pk):
    try:
        autor = Author.objects.get(pk=pk)
    except:
        return Response({"error": "Item not found"}, status=status.HTTP_400_BAD_REQUEST)

    autor.delete()
    return Response(status=status.HTTP_200_OK)
