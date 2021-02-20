from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
]

def response_error_handler(request, exception=None):
    pass
    
handler404 = 'Gaido.views.page_not_found'