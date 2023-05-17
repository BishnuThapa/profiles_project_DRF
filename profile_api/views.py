from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.


class HelloApiView(APIView):
    """Test API View"""
    def get(self,request,format=None):
        """Returns a list of APIView Features"""
        return Response({'message':'Hello from Get Method'})