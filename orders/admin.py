from django.contrib import admin
from .models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        "foydalanuvchi_id",
        "status",
        "total_price",
        "buyurtma_sanasi",
        "order_date",
    )

    list_filter = ("status", "buyurtma_sanasi")

    search_fields = ("foydalanuvchi_id",)

    ordering = ("-buyurtma_sanasi",)
# Register your models here.
