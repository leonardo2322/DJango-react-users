from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework import filters
from .serializers.serilizerGeneral import UserProfileSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.settings import api_settings
from rest_framework.authtoken.views import ObtainAuthToken
from .permisos.permissions import PermissionsOwnProfile
from .models import UserProfile
# Create your views here.

class helloWorld(APIView):
    def get(self, request, format=None):
        hi = ['hello world','fucking world']
        return Response({'message':'success','quer':hi})

class ViewsetModel(ModelViewSet):
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (PermissionsOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name','email','phone',)

class UserLogin(ObtainAuthToken):
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES