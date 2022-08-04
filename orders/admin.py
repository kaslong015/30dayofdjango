from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['size', 'order_status', 'quantity', 'update_at']
    list_filter = ['size', 'order_status', 'quantity', 'update_at']
# admin.site.register(Order)
