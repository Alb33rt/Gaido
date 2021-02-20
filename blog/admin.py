from django.contrib import admin

from .models import Blogpost, Type, Region

# Register your models here.
admin.site.register(Blogpost)
admin.site.register(Type)
admin.site.register(Region)