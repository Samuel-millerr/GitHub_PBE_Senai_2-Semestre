from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.models import Book
from api.serializers import BookSerializer

@api_view(['GET'])
def books_list(request):
    queryset = Book.objects.all()
    serializer = BookSerializer(queryset, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def book_list(request, pk):
    book = Book.objects.get(pk = pk)
    serializer = BookSerializer(book)
    return Response(serializer.data)

@api_view(['GET', 'POST'])
def book_create(request):
    if request.method == "GET":
        book_model = Book.objects.model()
        serializer = BookSerializer(book_model)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = BookSerializer(data = request.data)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else: 
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
        
@api_view(['GET', 'PUT'])
def book_update(request):
    pass