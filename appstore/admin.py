from django.contrib import admin
from embed_video.admin import AdminVideoMixin
from .models import Item
from .models import Customers, addUpComing, movies, addMessage, Profile

admin.site.register([Customers,addUpComing,movies,addMessage,Profile])

class MyModelAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass

admin.site.register(Item, MyModelAdmin)