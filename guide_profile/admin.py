from django.contrib import admin

from .models import *

class GuideProfileAdmin(admin.ModelAdmin):
    list_display = ('__str__', )


admin.site.register(GuideProfile, GuideProfileAdmin)
