from django.db import models
from django.utils.translation import gettext_lazy as _

from django.contrib.auth.models import User


class Language(models.Model):
    class Meta:
        verbose_name = _('Мова')
        verbose_name_plural = _('Мови')

    language_en = models.CharField(max_length=256, null=True, blank=True)
    language_ru = models.CharField(max_length=256, null=True, blank=True)
    language_ua = models.CharField(max_length=256, null=True, blank=True)

    def __str__(self):
        return self.language_en or "Language"


class GuideProfile(models.Model):

    class Meta:
        verbose_name = _('Профіль Гіда')
        verbose_name_plural = _('Профілі гідів')

    auth_user = models.OneToOneField(User, on_delete=models.CASCADE, null=False, blank=False)
    first_name = models.CharField(max_length=256, null=False, blank=False)
    last_name = models.CharField(max_length=256, null=False, blank=False)
    date_of_birth = models.DateField(null=False, blank=False)
    phone = models.CharField(max_length=256, null=False, blank=False)
    email = models.EmailField(max_length=256, null=False, blank=False)
    personal_description = models.CharField(max_length=256, null=False, blank=False)
    language = models.ManyToManyField(Language, related_name='profile_languages', null=False, blank=False)

    validation_image = models.ImageField(upload_to='media/profile_validation')
    profile_image = models.ImageField(upload_to=f'media/{id}/')

    is_valid = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

    # def validation_success_mail(self):
    #     return
