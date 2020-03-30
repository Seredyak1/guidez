from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django import forms
from django.contrib.auth.models import Group

from django.contrib.auth import get_user_model
User = get_user_model()


class UserCreationForm(forms.ModelForm):
    """Use for creation new user from admin panel"""
    class Meta:
        model = User
        fields = ('email',)

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class CustomUserAdmin(UserAdmin):
    """Add custom user ot Admin panel"""
    add_form = UserCreationForm
    list_display = ('email', 'first_name', 'last_name', 'is_valid')
    list_filter = ('email',)
    ordering = ("email",)

    fieldsets = (
        (None, {'fields': ('email', 'password', 'first_name', 'last_name', 'city', 'languages', 'validation_image',
                           'is_valid', 'is_active', 'is_superuser')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password', 'first_name', 'last_name', 'is_active', 'is_superuser',)}
         ),
    )

    filter_horizontal = ()

admin.site.register(User, CustomUserAdmin)
admin.site.unregister(Group)
