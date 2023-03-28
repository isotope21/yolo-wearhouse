from django.contrib import admin
from .models import Hotel

class imageAdmin(admin.ModelAdmin):
    list_display = ["name", "hotel_Main_Img"]

admin.site.register(Hotel, imageAdmin)