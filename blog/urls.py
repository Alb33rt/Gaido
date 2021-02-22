from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('create/', views.createPost, name="create"),
    path('post/<uuid:uuid>', views.blogpost, name="blogpost"),
    path('<uuid:uuid>/edit', views.editpost, name="editpost"),
    path('<uuid:uuid>/comment', views.comment, name="comment"),
]