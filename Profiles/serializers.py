from rest_framework import serializers
from .models import Profile, CustomUser

class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for the CustomUser model.
    """
    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'username', 'date_joined']
        read_only_fields = ['id', 'date_joined']
        
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'user', 'bio', 'profile_picture']
        read_only_fields = ['id', 'user']