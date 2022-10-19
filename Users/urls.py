import imp
from operator import imod
from django.urls import path, include
from .views import helloWorld,ViewsetModel , UserLogin
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('profile',ViewsetModel)

urlpatterns= [
    path('api/', helloWorld.as_view()),
    path('', include(router.urls)),
    path('login/', UserLogin.as_view())
]
