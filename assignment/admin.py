from django.contrib import admin

# Register your models here.
from .models import Client, User

admin.site.register(Client)
admin.site.register(User)
