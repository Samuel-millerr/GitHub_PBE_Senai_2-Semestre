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

@api_view(['POST'])
def publisher_create(resquest):
    serializer = PublisherSerializer(data = resquest.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)