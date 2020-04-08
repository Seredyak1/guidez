from django.contrib import admin

from .models import GuidePersonalTour


class GuidePersonalTourAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'created_at',)


admin.site.register(GuidePersonalTour, GuidePersonalTourAdmin)
