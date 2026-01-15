from django.contrib import admin
from .models import ChocolateProduct
# Register your models here.
@admin.register(ChocolateProduct)
class ChocolateProductAdmin(admin.ModelAdmin):
    list_display = (
        "nomi",
        "turi",
        "category",
        "narxi",
        "miqdori",
    )

    list_filter = (
        "turi",
        "category",
    )

    search_fields = (
        "nomi",
        "tavsifi",
    )


