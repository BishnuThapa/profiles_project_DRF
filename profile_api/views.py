from django.shortcuts import render
from rest_framework import status
from rest_framework.filters import SearchFilter,OrderingFilter
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet,ModelViewSet
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .permissions import *
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
    filter_backends=(SearchFilter,OrderingFilter,)
    search_fields=('name','email',)


class UserLoginApiView(ObtainAuthToken):
    """ Handle Creating user authentication tokens"""
    renderer_classes= api_settings.DEFAULT_RENDERER_CLASSES

class UserProfileFeedViewSets(ModelViewSet):
    queryset=ProfileFeedItem.objects.all()
    serializer_class=ProfileFeedItemSerializer
    authentication_classes=(TokenAuthentication,)
    permission_classes=(UpdateOwnStatus,IsAuthenticatedOrReadOnly)

    def perform_create(self, serializer):
        """Sets user profile to the logged in user """
        return serializer.save(user=self.request.user)