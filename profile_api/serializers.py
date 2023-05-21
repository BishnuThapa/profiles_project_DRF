from rest_framework import serializers
from .models import *

class HelloSerializer(serializers.Serializer):
    """Serializer a name field for testing our APIView"""
    name=serializers.CharField(max_length=10)


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserProfile
        fields=['id','email','name','password']
        #password for not showing in listing users
        extra_kwargs={
            'password': {
                'write_only':True,
                'style':{'input_type':'password'}
            }
        }
    def create(self, validated_data):
        """Create & return new user"""
        user=UserProfile.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']
        )
        return user  
    
class ProfileFeedItemSerializer(serializers.ModelSerializer):
    class Meta:
        model=ProfileFeedItem
        fields=['id','user','status_text','created_on']
        extra_kwargs={
            'user':{'read_only':True}
        }