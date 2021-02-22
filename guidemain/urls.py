from django.urls import path  

from . import views

# Write the urls here.
urlpatterns = [
    path('', views.index, name='full'),
    path('sorted', views.specficview, name="specific")
]