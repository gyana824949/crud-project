from django.contrib import admin
from enroll.models import *
# Register your models here.
@admin.register(user)
class userAdmin(admin.ModelAdmin):
    list_display=('id','name','email','password')