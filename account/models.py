from django.db import models
from django.contrib.auth.models import User


# Дополнительные параметры пользователя
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    status = models.CharField(max_length=50, blank=True)
    balance = models.DecimalField(decimal_places=1, max_digits=14, default=0, verbose_name="Бaланс")

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = "Профиль"
        verbose_name_plural = "Профили"


# Кейсы, которые пользователь покупал
class UserCase(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    case_id = models.IntegerField()
    name = models.CharField(max_length=20, verbose_name="Название кейса")
    price = models.DecimalField(max_digits=100, decimal_places=0, verbose_name="Цена кейса")
    image = models.ImageField("Фотография кейса", upload_to='case/')


# Оружия, которые выпали пользователю
class UserGun(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='weapon/', blank=True, verbose_name="Фотография оружия")
    name = models.CharField(max_length=20, verbose_name="Название оружия")
    price = models.DecimalField(max_digits=100, decimal_places=0, verbose_name="Цена оружия")
    rarity = models.CharField(max_length=20, blank=True)
