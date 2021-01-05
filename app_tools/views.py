from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import (
    CaseSerializer,
    WeaponSerializer,
    WeaponLineSerializer,
    ProfileListSerializer,
    ProfileDetailSerializer,
)
from app_tools.models import Weapon, Case, WeaponLine
from account.models import User, Profile
from .services import case_service
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class CaseListView(generics.ListAPIView):
    queryset = Case.objects.all()
    serializer_class = CaseSerializer


class CaseDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Case.objects.all()
    serializer_class = CaseSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, ]


class WeaponListView(generics.ListAPIView):
    queryset = Weapon.objects.all()
    serializer_class = WeaponSerializer


class WeaponDetailView(generics.RetrieveAPIView):
    queryset = Weapon.objects.all()
    serializer_class = WeaponSerializer


class WeaponLineView(generics.ListAPIView):
    queryset = WeaponLine.objects.all()
    serializer_class = WeaponLineSerializer


class ProfileListView(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileListSerializer


class ProfileDetailView(generics.RetrieveUpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileDetailSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, ]



