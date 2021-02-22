from django.contrib import admin

from .models import Blogpost, Type, Region, Comment

class BlogpostAdmin(admin.ModelAdmin):
    model = Blogpost
    list_display = ['author', 'category', 'region', 'uuid', 'time_created']

# Register your models here.
admin.site.register(Blogpost, BlogpostAdmin)
admin.site.register(Type)
admin.site.register(Region)
admin.site.register(Comment)