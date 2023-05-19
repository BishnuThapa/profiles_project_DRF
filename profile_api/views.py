from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet,ModelViewSet
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from .permissions import UpdateOwnProfile
from .serializers import *
from .models import *
# Create your views here.

class HelloViewSet(ViewSet):
    serializer_class=HelloSerializer
    """ Test API Viewset"""

    def list(self,request):
        return Response({'message':'Hello'})
    
    def create(self,request):
        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid():
            name=serializer.validated_data.get('name')
            message=f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
    def retrieve(self,request,pk=None):
        return Response({'Method':'GET'})
    
    def update(self,request,pk=None):
        return Response({'Method':'PUT'})
    def partial_update(self,request,pk=None):
        return Response({'Method':'PATCH'})

    def destroy(self,request,pk=None):
        return Response({'Method':'DESTROY'})


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

    def put(self,request,pk=None):
        """ Handle updating an object"""
        return Response({'method':'PUT'})
    
    def patch(self,request,pk=None):
        """ Handle partial update to an object"""

        return Response({'method':'PATCH'})
    
    def delete(self,request,pk=None):
        """ Handle delete an object"""
        return Response({'method':'DELETE'})


class UserProfileViewSet(ModelViewSet):
    queryset=UserProfile.objects.all()
    serializer_class=ProfileSerializer
    authentication_classes=(TokenAuthentication,)
    permission_classes=(UpdateOwnProfile,)
