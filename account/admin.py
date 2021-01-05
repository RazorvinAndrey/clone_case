from django.contrib import admin
from .models import *


admin.site.register(Profile)
# admin.site.register(UserCase)
admin.site.register(UserGun)

# Не забудь после разработки удалить лишние поля а именно usercase