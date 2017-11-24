from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^chatting/$', views.chat, name='chatting'),
]
