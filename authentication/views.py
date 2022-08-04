from django.shortcuts import render
from yaml import serialize
from rest_framework import generics, status
from rest_framework.response import Response
from .models import User
# Create your views here.
from .serializers import UserCreationSerializer


class HelloAuthView(generics.GenericAPIView):

    def get(self, request, *args, **kwargs):
        return Response(data={"message": "hello Auth response"}, status=status.HTTP_200_OK)


class UserCreationView(generics.GenericAPIView):

    serializer_class = UserCreationSerializer

    def post(self, request):
        data = request.data

        serialize = self.serializer_class(data=data)
        if serialize.is_valid():
            serialize.save()
            return Response(data=serialize.data, status=status.HTTP_201_CREATED)
        return Response(data=serialize.errors, status=status.HTTP_400_BAD_REQUEST)
