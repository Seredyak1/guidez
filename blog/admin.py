from django.contrib import admin

from .models import Blog, Comment


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0


class BlogAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'created_at',)
    inlines = (CommentInline,)


admin.site.register(Blog, BlogAdmin)
