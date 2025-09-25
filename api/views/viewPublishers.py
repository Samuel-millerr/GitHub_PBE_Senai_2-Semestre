from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response

# Autenticação
from rest_framework.permissions import IsAuthenticated

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter

from api.models import Publisher
from api.serializers import PublisherSerializer

class PublisherView(APIView):
    # permission_classes = [IsAuthenticated]

    def get(self, request, pk=None):
        if pk:
            try:
                publisher = Publisher.objects.get(pk = pk)
                serializer = PublisherSerializer(publisher)
                return Response(serializer.data)
            except:
                return Response({"error": "Publisher not found"})
        else:
            queryset = Publisher.objects.all()
            serializer = PublisherSerializer(queryset, many=True)
            return Response(serializer.data)

    def post(self, request):
        serializer = PublisherSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk=True):
        try:
            publisher = Publisher.objects.get(pk = pk)
        except: 
            return Response({"error": "Publisher not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = PublisherSerializer(publisher, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST) 
    
    def patch(self, request, pk=True):
        try:
            publisher = Publisher.objects.get(pk = pk)
        except:
            return Response({"error": "Publisher not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = PublisherSerializer(publisher, data=request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else: 
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
                               
    def delete(self, request, pk=True):
        try:
            publisher = Publisher.objects.get(pk=pk)
        except:
            return Response({"error": "Publisher not found"}, status=status.HTTP_404_NOT_FOUND)
        
        publisher.delete()
        return Response({"message": "Publisher successfully delete"}, status=status.HTTP_200_OK)
    