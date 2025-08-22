from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.models import Publisher
from api.serializers import PublisherSerializer

@api_view(['GET'])
def publishers_list(request):
    queryset = Publisher.objects.all()
    serializer = PublisherSerializer(queryset, many= True)
    return Response(serializer.data)

@api_view(["GET"])
def publisher_list(request, pk):
    try:
        publisher = Publisher.objects.get(pk=pk)
        serializer = PublisherSerializer(publisher)
        return Response(serializer.data)
    except:
        return Response({"error": "Publisher not found"}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET', 'POST'])
def publisher_create(resquest):
    if resquest.method == "GET":
        publisher_model= Publisher.objects.model()
        serializer = PublisherSerializer(publisher_model)
        return Response(serializer.data)
    
    elif resquest.method == "POST":
        serializer = PublisherSerializer(data = resquest.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT'])
def publisher_update(request, pk):
    try: 
       publisher = Publisher.objects.get(pk=pk)
    except Publisher.DoesNotExist:
          return Response({"error": "Publisher not found"},status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        serializer = PublisherSerializer(publisher)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = PublisherSerializer(publisher, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def publisher_delete(request, pk):  
    try:
        publisher = Publisher.objects.get(pk= pk)
    except:
        return Response({"error": "Publisher not found"}, status=status.HTTP_404_NOT_FOUND)

    publisher.delete()
    return Response({"message": "Publisher successfully deleted"}, status=status.HTTP_200_OK)