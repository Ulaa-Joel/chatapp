# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Room, Message

# Register your models here.
admin.site.register(Room)
admin.site.register(Message)
