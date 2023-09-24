from django.urls import path
from web.views import IndexPage

urlpatterns = [
    path('',  IndexPage.as_view(), name='index'),

]
