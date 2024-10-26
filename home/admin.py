from django.contrib import admin

# Register your models here.
from .models import home   # .: the admin and model in same folder

admin.site.register(home)