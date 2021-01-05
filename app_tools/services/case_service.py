from account.models import UserCase, UserGun, User
from app_tools.models import WeaponLine, Case

import random


def get_user(user_id):
    return User.objects.get(pk=user_id)


def get_case(case_id):
    return Case.objects.get(pk=case_id)


def get_weapon_line(int_wep):
    return WeaponLine.objects.all().order_by('-id')[:int_wep]


def buy_case(user_id, case_id):
    user = User.objects.get(pk=user_id)
    current_case = Case.objects.get(pk=case_id)
    weapons = WeaponLine.objects.all()
    weapon_win = None
    not_enough = False
    if user.profile.balance > current_case.price:
        user.profile.balance -= current_case.price
        user.profile.save()
        weapon_win = create_objects_after_open_case(user, current_case)
        if len(weapons) > 12:
            weapons[0].delete()
    else:
        not_enough = True
    return weapon_win


def create_objects_after_open_case(user, current_case):
    random_gun_win = random.choice(current_case.weapon.all())
    UserCase.objects.create(
        user=user,
        case_id=current_case.pk,
        name=current_case.name,
        price=current_case.price,
        image=current_case.image
    )
    UserGun.objects.create(
        user=user,
        name=random_gun_win.name,
        price=random_gun_win.price,
        image=random_gun_win.image,
        rarity=random_gun_win.rarity.name
    )
    WeaponLine.objects.create(
        image=random_gun_win.image,
        name=random_gun_win.name,
        rarity=random_gun_win.rarity.name
    )
    return random_gun_win
