from django.contrib import admin
from .models import Topic, Entry

# Регистрация моделей в админке
admin.site.register(Topic)
admin.site.register(Entry)
