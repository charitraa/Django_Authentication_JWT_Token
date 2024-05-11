from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserRegistrationSerializer , UserLoginSerializer
from rest_framework import status
from django.contrib.auth import authenticate

class UserRgistrationView(APIView):
    def post(self, request ):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Regisation successful'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class USerLoginView(APIView):
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email = serializer.data.get('email')
            password = serializer.data.get('password')
            user = authenticate(email=email, password=password)
            if user is not None :
                return Response({'msg':'Login successful'}, status=status.HTTP_200_OK)
            else:
                return Response({'msg':'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)