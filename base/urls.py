from .views import slide
from django.urls import path

urlpatterns = [
    path('', slide, name='slide')
]
