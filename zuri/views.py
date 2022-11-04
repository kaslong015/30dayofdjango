from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from . import serializers

# Create your views here.


class HelloZuriView(generics.GenericAPIView):

    def get(self, request):
        return Response(data={
            "slackUsername": "kaslong", "backend": True, "age": 25, "bio": "i love coding."
        }, status=status.HTTP_200_OK)


class Compute:

    def addition(x, y):
        return x + y

    def subtraction(x, y):
        return x - y

    def multiplication(x, y):
        return x * y


class MathView(generics.GenericAPIView):
    '''
    set serializer class and queryset

    '''
    serializer_class = serializers.MathSerializer

    def get(self, request):
        return Response(data={
            "slackUsername": "kaslong", "backend": True, "age": 25, "bio": "i love coding."
        }, status=status.HTTP_200_OK)

    def post(self, request):
        '''
        get posted data validate over serializer save and return data
        else throw error
        '''

        data = request.data
        serializer = self.serializer_class(data=data)

        if serializer.is_valid():
            print(serializer.data)
            if serializer.data['operation_type'] == 'MULTIPLICATION':
                return Response(data={
                    "slackUsername": "kaslong",
                    "result": Compute.multiplication(serializer.data['x'], serializer.data['y']),
                    "operation_type": 'multiplication'

                }, status=status.HTTP_201_CREATED)
            if serializer.data['operation_type'] == 'ADDITION':
                return Response(data={
                    "slackUsername": "kaslong",
                    "result": Compute.addition(serializer.data['x'], serializer.data['y']),
                    "operation_type": 'addition'

                }, status=status.HTTP_201_CREATED)
            if serializer.data['operation_type'] == 'SUBTRACTION':
                return Response(data={
                    "slackUsername": "kaslong",
                    "result": Compute.subtraction(serializer.data['x'], serializer.data['y']),
                    "operation_type": 'subtraction'

                }, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
