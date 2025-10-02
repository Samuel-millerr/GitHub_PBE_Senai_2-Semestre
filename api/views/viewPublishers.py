from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter

from api.models import Publisher
from api.serializers import PublisherSerializer


""" Um dos tipos de realizar um criação de um metódo dentro do django é atráves de classes, assim todos os seus metódos
serão funções dentro dessa classe """
class PublisherView(APIView):
    def get_publisher(self, pk):
        """ Função utilizada para pegar um author somente, utilizada em metódos onde é necessário uma primary key """
        publisher = Publisher.objects.get(pk = pk)
        return publisher

    # permission_classes = [IsAuthenticated]

    """ METÓDO POST """
    def post(self, request):
        serializer = PublisherSerializer(data = request.data)
        if serializer.is_valid():
            for publisher in Publisher.objects.all():
                if str(publisher.nome) == request.data["nome"]:
                    nome = request.data["nome"]
                    return Response({"error": f"a editora com o nome {nome} já está cadastrado no banco"}, status=status.HTTP_409_CONFLICT)
                if str(publisher.cnpj) == request.data["cnpj"]:
                    cnpj = request.data["cnpj"]
                    return Response({"error": f"o cnpj {cnpj} já está cadastrado no banco de dados"})  
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({"error": "wrong parameters"}, status=status.HTTP_400_BAD_REQUEST)

    """ METÓDO GET"""
    def get(self, request, pk=None):
        if pk:
            try:
                publisher = self.get_publisher(pk)
                serializer = PublisherSerializer(publisher)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except:
                return Response({"error": "publisher not found"}, status=status.HTTP_404_NOT_FOUND)
        else:
            queryset = Publisher.objects.all()
            serializer = PublisherSerializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
    
    """ METÓDO PATCH """
    def patch(self, request, pk=True):
        try:
            publisher = self.get_publisher(pk)
        except:
            return Response({"error": "publisher not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = PublisherSerializer(publisher, data=request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"message": "wrong parameters"}, status=status.HTTP_400_BAD_REQUEST)

    """ METÓDO DELETE """
    def delete(self, request, pk=True):
        try:
            publisher = self.get_publisher(pk)
        except:
            return Response({"error": "publisher not found"}, status=status.HTTP_404_NOT_FOUND)
        
        publisher.delete()
        return Response({"message": "publisher successfully delete"}, status=status.HTTP_204_NO_CONTENT)
    