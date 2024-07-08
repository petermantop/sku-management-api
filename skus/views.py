from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from skus.models import Sku
from skus.serializers import SkuSerializer

@api_view(['GET', 'POST'])
def sku_list(request):
    """
    List all skus, or create a new sku.
    """
    if request.method == 'GET':
        skus = Sku.objects.all()
        serializer = SkuSerializer(skus, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SkuSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'PUT', 'DELETE'])
def sku_detail(request, pk):
    """
    Retrieve, update or delete a sku.
    """
    try:
        sku = Sku.objects.get(pk=pk)
    except Sku.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SkuSerializer(sku)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = SkuSerializer(sku, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        sku.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)