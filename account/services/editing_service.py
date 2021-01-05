from account.models import *


def get_user(user_id):
    return User.objects.get(pk=user_id)


def get_weapons_of_profile(user_id):
    return UserGun.objects.filter(user=user_id).order_by('-id')


def get_cases_of_profile(user_id):
    return UserCase.objects.filter(user=user_id)


def get_current_gun(wep_pk):
    return UserGun.objects.get(pk=wep_pk)


def sell_gun(user, weapon):
    user.profile.balance = user.profile.balance + weapon.price
    weapon.delete()
    user.profile.save()
    return None


def reduct_status(user_id, new_text):
    user = get_user(user_id)
    user.profile.status = new_text
    user.profile.save()
    return None


def register(username, email, password, password2):
    error = False
    if password == password2:
        User.objects.create_user(username, email, password)
        user = User.objects.get(username=username)
        Profile.objects.create(user=user, status="")
        return None
    else:
        error = True
    return error
