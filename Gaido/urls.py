from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('denied', views.perm_denied, name="no_perm"),
]

def response_error_handler(request, exception=None):
    pass
    
handler404 = 'Gaido.views.page_not_found'