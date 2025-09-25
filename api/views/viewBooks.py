from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView
from rest_framework.response import Response

#Autenticação
from rest_framework.permissions import IsAuthenticated 

from api.models import Book
from api.serializers import BookSerializer

class BookView(APIView):
    def get(self, request, pk=None):
        if pk:
            try:
                book = Book.objects.get(pk = pk)
                serializer = BookSerializer(book)
                return Response(serializer.data)
            except:
                return Response({"error": "Publisher not found"})
        else:
            queryset = Book.objects.all()
            serializer = BookSerializer(queryset, many=True)
            return Response(serializer.data)
        
    def post(self, request):
        serializer = BookSerializer(data = request.data)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def books_list(request):
    queryset = Book.objects.all()
    serializer = BookSerializer(queryset, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def book_list(request, pk):
    book = Book.objects.get(pk = pk)
    serializer = BookSerializer(book)
    return Response(serializer.data)

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def book_create(request):
    if request.method == 'GET':
        book_model = Book.objects.model()
        serializer = BookSerializer(book_model)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = BookSerializer(data = request.data)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else: 
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
        
@api_view(['GET', 'PUT'])
@permission_classes([IsAuthenticated])
def book_update(request, pk):
    try:
        book = Book.objects.get(pk =pk)
    except:
        return Response ({"error": "Book not found"}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = BookSerializer(book)
        return Response (serializer.data)
    elif request.method == 'PUT':
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PATCH'])
@permission_classes([IsAuthenticated])
def book_patch(request, pk):
    try:
        book = Book.objects.get(pk = pk)
    except:
        return Response({"error": "Book not found"}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET': 
        serializer = BookSerializer(book)
        return Response(serializer.data)
    elif request.method == 'PATCH':
        serializer = BookSerializer(book, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else: 
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
        
@api_view(['DELETE'])
def book_delete(request, pk):
    try:
        book = Book.objects.get(pk = pk)
    except:
        return Response({"error": "Book not found"}, status=status.HTTP_404_NOT_FOUND)
    
    book.delete()
    return Response({"message":"Book successfully delete"}, status=status.HTTP_200_OK)
