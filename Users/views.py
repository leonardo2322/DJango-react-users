import imp
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

class helloWorld(APIView):
    def get(self, request, format=None):
        hi = ['hello world','fucking world']
        return Response({'message':'success','quer':hi})