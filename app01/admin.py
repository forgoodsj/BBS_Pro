# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import BBS,Category,BBS_user
# Register your models here.
class BBSAdmin(admin.ModelAdmin):
    list_display = ('title','summary','content','author','view_count','ranking','created_at','updated_at')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','administrator')

class BBS_userAdmin(admin.ModelAdmin):
    list_display = ('user', 'signature','photo')

admin.site.register(BBS,BBSAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(BBS_user,BBS_userAdmin)

