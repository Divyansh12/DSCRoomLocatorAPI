from django.contrib import admin

# Register your models here.

from django.contrib import admin
from django.apps import apps

app = apps.get_app_config('roomlocator')

class PersonAdmin(admin.ModelAdmin):
    search_fields = ['room','number','isAvailable','day','time']

for model_name, model in app.models.items():
    model_admin = type(model_name + "Admin", (PersonAdmin, ), {'list_display': tuple([field.name for field in model._meta.fields])})
    admin.site.register(model, model_admin)
    list_filter = '__all__'
