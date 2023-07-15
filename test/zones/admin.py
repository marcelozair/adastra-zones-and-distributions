from django.contrib import admin

from zones.models import Zone, Distribution


class DistributionInline(admin.TabularInline):
    model = Distribution


class ZoneAdmin(admin.ModelAdmin):
    model = Zone
    inlines = [
        DistributionInline,
    ]


admin.site.register(Zone, ZoneAdmin)
