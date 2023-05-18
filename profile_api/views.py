from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import HelloSerializer
# Create your views here.


class HelloApiView(APIView):
    serializer_class=HelloSerializer
    """Test API View"""
    def get(self,request,format=None):
        """Returns a list of APIView Features"""
        return Response({'message':'Hello from Get Method'})
    
    def post(self,request):
        """Create a hello message with our name"""
        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid():
            name=serializer.validated_data.get('name')
            message=f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
