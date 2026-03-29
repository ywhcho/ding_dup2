from django.contrib import admin
from .models import Medicine

@admin.register(Medicine)
class MedicineAdmin(admin.ModelAdmin):
    list_display = ("name", "ingredient", "company")
    search_fields = ("name", "ingredient", "company")
