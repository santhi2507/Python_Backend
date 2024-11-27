from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from InheritCardianlity.models import User
from InheritCardianlity.serializers import UserModelSerializer


# Create your views here.

class UserListCreateAPIView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer

