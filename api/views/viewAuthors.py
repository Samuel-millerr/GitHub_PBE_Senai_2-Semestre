from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated

from api.models import Author
from api.serializers import AuthorSerializer

import pandas as pd
import os

class AuthorView(APIView):
    def get_author(self, pk):
        """ Função utilizada para pegar um author somente, utilizada em metódos onde é necessário uma primary key """
        author = Author.objects.get(pk = pk)
        return author

    # permission_classes = [IsAuthenticated]

    """ METÓDO POST """
    def post(self, request):
        serializer = AuthorSerializer(data = request.data)
        if serializer.is_valid(): 
            for author in Author.objects.all():
                if str(author.nome) == request.data["nome"] and str(author.sobrenome) == request.data["sobrenome"]:
                    return Response({"error": f"o autor {request.data["nome"]} já está cadastrado no banco de dados!"} , status=status.HTTP_409_CONFLICT)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({"error": "wrong parameters"}, status=status.HTTP_400_BAD_REQUEST)

    """ METÓDO GET"""
    def get(self, request, pk=None):
        if pk:
            try:
                author = Author.objects.get(pk = pk)
                serializer = AuthorSerializer(author)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except:
                return Response({"error": "author not found"}, status=status.HTTP_404_NOT_FOUND)
        else:
            queryset = Author.objects.all()
            serializer = AuthorSerializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
    """ METÓDO PATCH """
    def patch(self, request, pk=True):
        try:
            author = self.get_author(pk)
        except:
            return Response({"error": "author not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = AuthorSerializer(author, data=request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"message": "wrong parameters"}, status=status.HTTP_400_BAD_REQUEST)

    """ METÓDO DELETE"""
    def delete(self, request, pk=True):
        try:
            author = self.get_author(pk)
        except:
            return Response({"error": "Author not found"}, status=status.HTTP_404_NOT_FOUND)
        
        author.delete()
        return Response({"message": "author successfully delete"}, status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
# @permission_classes([IsAuthenticated])
def author_create_csv(request):
    BASE_DIR = os.path.dirname(os.path.abspath(os.path.join(__file__, "../../")))
    if request.method == 'POST':
        documento = request.body.decode('utf-8')
        caminho_documento = os.path.join(BASE_DIR, "population", documento)
        if documento:
            df = pd.read_csv(caminho_documento, encoding="utf-8-sig")
            for index_linha in range(len(df)):
                autor = dict(df.iloc[index_linha])
                serializer = AuthorSerializer(data=autor)
                if serializer.is_valid():
                    serializer.save()

        return Response(documento)
