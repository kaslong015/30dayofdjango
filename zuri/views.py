from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response

# Create your views here.


class HelloZuriView(generics.GenericAPIView):

    def get(self, request):
        return Response(data={
            "slackUsername": "kaslong", "backend": True, "age": 25, "bio": "i love coding."
        }, status=status.HTTP_200_OK)
