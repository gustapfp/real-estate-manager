from django.contrib import admin

from real_state_manager.locations.models import Location

# Register your models here.


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ["id", "street", "city", "state", "country", "created_at"]
    search_fields = ["street", "city", "state", "cep"]
    list_filter = ["state", "city", "country", "created_at"]
