from django.contrib import admin

from .models import Listing


@admin.register(Listing)
class ListingAdmin(admin.ModelAdmin):
    class Meta:
        model = Listing
        
    readonly_fields = ("id", "slug", "created", "modified")
