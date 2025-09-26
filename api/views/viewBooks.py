from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated 

from api.models import Book
from api.serializers import BookSerializer

class BookView(APIView):
    def get_book(self, pk):
        book = Book.objects.get(pk = pk)
        return book
    
    # permission_classes = [IsAuthenticated]
    
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
            for book in Book.objects.all():
                if book.titulo == request.data["titulo"]:
                    return Response({"error": f"o livro {request.data["titulo"]} já está cadastrado no sistema"})
                if book.isbn == request.data["isbn"]:
                    return Response({"error": f"o livro com o isbn {request.data["isbn"]} já está cadastrado"})
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({"error": "wrong parameters"}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk=None):
        if pk:
            try:
                author = self.get_book(pk)
                serializer = BookSerializer(author)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except:
                return Response({"error": "author not found"}, status=status.HTTP_404_NOT_FOUND)
        else:
            queryset = Book.objects.all()
            serializer = BookSerializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
    
    def patch(self, request, pk=True):
        try: 
            author = self.get_book(pk)
        except:
            return Response({"error": "author not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = BookSerializer(author, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"error": "wrong parameters"}, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk=True):
        try:
            author = self.get_book(pk)
        except:
            return Response({"error": "author not found"}, status=status.HTTP_404_NOT_FOUND)
        
        author.delete()
        return Response({"message": "author successfully delete"}, status=status.HTTP_204_NO_CONTENT)