from .models import *

from django.contrib.auth.models import User
# from .services import editing_service

from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .serializers import (
    WeaponOfUserSerializer,
    CaseOfUserSerializer,
)
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


class WeaponOfUserListView(generics.ListAPIView):
    def get_queryset(self):
        return UserGun.objects.filter(user=self.request.user)
    serializer_class = WeaponOfUserSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, ]


class WeaponOfUserDetailView(generics.RetrieveAPIView):
    queryset = UserGun.objects.all()
    serializer_class = WeaponOfUserSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, ]


class CaseOfUserListView(generics.ListAPIView):
    def get_queryset(self):
        return UserGun.objects.filter(user=self.request.user)
    serializer_class = CaseOfUserSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, ]


class ExampleView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        unicode = str
        content = {
            'user': unicode(request.user),  # `django.contrib.auth.User` instance.
            'auth': unicode(request.auth),  # None
        }
        return Response(content)

