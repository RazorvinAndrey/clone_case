from abc import ABC

from rest_framework import serializers

from app_tools.models import Case, WeaponLine, Weapon
from account.models import Profile, User


class CaseSerializer(serializers.ModelSerializer):
    # Вывод мнформации о кейсах
    class Meta:
        model = Case
        fields = ["id", "name", "price", "image"]


class WeaponSerializer(serializers.ModelSerializer):
    # Вывод мнформации об оружии
    class Meta:
        model = Weapon
        fields = "__all__"


class WeaponLineSerializer(serializers.ModelSerializer):
    # Вывод ленты недавно выбитых оружий
    class Meta:
        model = WeaponLine
        fields = "__all__"


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class ProfileListSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field="username", read_only=True)

    class Meta:
        model = Profile
        fields = "__all__"


class ProfileDetailSerializer(serializers.ModelSerializer):
    user = UserDetailSerializer()

    class Meta:
        model = Profile
        fields = "__all__"
