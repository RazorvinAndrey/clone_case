from django.db import models


# Все кейсы сайта
class Case(models.Model):
    name = models.CharField(max_length=20, verbose_name="Название кейса")
    weapon = models.ManyToManyField('Weapon', verbose_name="Оружие")
    price = models.DecimalField(max_digits=100, decimal_places=0, verbose_name="Цена кейса")
    image = models.ImageField("Фотография кейса", upload_to='case/')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Кейс'
        verbose_name_plural = 'Кейсы'


# Все оружия сайта
class Weapon(models.Model):
    image = models.ImageField(upload_to='weapon/', verbose_name="Фотография оружия")
    name = models.CharField(max_length=20, verbose_name="Название оружия")
    price = models.DecimalField(max_digits=100, decimal_places=0, verbose_name="Цена оружия")
    rarity = models.ForeignKey('Rarity', verbose_name="Уровень редкости", on_delete=models.CASCADE)
    type_of_weapon = models.ForeignKey('TypeOfWeapon', verbose_name="Тип оружия", on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Оружие'
        verbose_name_plural = 'Оружия'


# Лента выбитых оружий
class WeaponLine(models.Model):
    image = models.ImageField(upload_to='weapon/', verbose_name="Фотография оружия")
    name = models.CharField(max_length=20, verbose_name="Название оружия")
    rarity = models.CharField(max_length=20, blank=True)


# Уровень редкости оружия
class Rarity(models.Model):
    name = models.CharField(max_length=20, verbose_name="Уровень редкости")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Уровень редкости оружия"
        verbose_name_plural = "Уровени редкости оружий"


# Тип оружия
class TypeOfWeapon(models.Model):
    type_name = models.CharField(max_length=20, verbose_name="Тип оружия")

    def __str__(self):
        return self.type_name

    class Meta:
        verbose_name = "Вид оружия"
        verbose_name_plural = "Виды оружий"






