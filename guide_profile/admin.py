from django.contrib import admin


from .models import *


class LanguageAdmin(admin.ModelAdmin):
    list_display = ('__str__',)


class GuideProfileAdmin(admin.ModelAdmin):
    list_display = ('__str__', )
    readonly_fields = ["headshot_image"]

    def headshot_image(self, obj):
        return mark_safe('<img src="{url}" width="360" height=240 />'.format(
            url = obj.validation_image.url,
            )
    )


admin.site.register(GuideProfile, GuideProfileAdmin)
admin.site.register(Language, LanguageAdmin)
