from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserRegistrationSerializer , UserLoginSerializer, UserProfileSerializer
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
       'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

class UserRgistrationView(APIView):
    def post(self, request ):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token = get_tokens_for_user(user)
            return Response({'token':token,'msg':'Regisation successful'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class USerLoginView(APIView):
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email = serializer.data.get('email')
            password = serializer.data.get('password')
            user = authenticate(email=email, password=password)
            if user is not None :
                token = get_tokens_for_user(user)
                return Response({'token':token,'msg':'Login successful'}, status=status.HTTP_200_OK)
            else:
                return Response({'msg':'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)
            
class userProfileView(APIView):
    def get(self, request):
        user = request.user
        permission_classes = [IsAuthenticated]
        serializer = UserProfileSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)