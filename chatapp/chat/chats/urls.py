from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'chats/$', views.home, name='home'),
    url(r'^chats/(?P<room>\w+)/', views.room, name='room'),
    url(r'chats/checkview', views.checkview, name='checkview'),
    url(r'chats/send', views.send, name='send'),
    url(r'chats/getMessages/(?P<room>\w+)/', views.getMessages, name='getMessages'),
]