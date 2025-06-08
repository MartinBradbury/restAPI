from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Profile, CustomUser
from .serializers import UserSerializer, ProfileSerializer
from rest_framework import generics

class CustomUserList(generics.ListAPIView):
    """
    API view to list all custom users.
    """
    serializer_class = UserSerializer
    queryset = CustomUser.objects.all()
    
    CustomUser.objects.all().order_by('-date_joined')
    
class UserProfileList(generics.APIView):
    """
    API view to retrieve a user's profile by user ID.
    """
    serializer_Class = ProfileSerializer
    queryset = Profile.objects.all()
    
    Profile.objects.all().order_by('-user__date_joined')