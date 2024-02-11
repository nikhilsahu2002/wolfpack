from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from app.models import Data
from app.serializer import DataSerializer
# Create your views here.

@api_view(['GET'])
def GetData(req):
    app = Data.objects.all()
    serializer = DataSerializer(app, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def postData(request):
    serializer = DataSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
