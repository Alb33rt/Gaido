from django.contrib import admin

from .models import Blogpost, Type, Region, Comment

# Register your models here.
admin.site.register(Blogpost)
admin.site.register(Type)
admin.site.register(Region)
admin.site.register(Comment)