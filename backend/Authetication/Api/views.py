from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Customer
from .serializers import CustomerSerializer

# Create your views here.
@api_view()
def post(request):
    user = Customer.objects.all()
    serializer = CustomerSerializer(user , many =True)
    return Response(serializer.data)
