from rest_framework import serializers
from account.models import UserGun, UserCase, User, Profile


class WeaponOfUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserGun
        fields = "__all__"


class CaseOfUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCase
        fields = "__all__"


