from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.safestring import mark_safe

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
    date_of_birth = models.DateField(null=True, blank=True)
    phone = models.CharField(max_length=256, null=True, blank=True)
    email = models.EmailField(max_length=256, null=True, blank=True)
    personal_description = models.TextField(null=True, blank=True)
    language = models.ManyToManyField(Language, related_name='profile_languages', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    validation_image = models.ImageField(upload_to='profile_validation')
    profile_image = models.ImageField(upload_to=f'{str(id)}/')

    is_valid = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

    # def validation_success_mail(self):
    #     return


class GuideProfileFeedback(models.Model):

    class Meta:
        verbose_name_plural = _('Відгуки про гідів')

    profile = models.ForeignKey(GuideProfile, on_delete=models.CASCADE, null=False, blank=False)
    name = models.CharField(max_length=256, null=False, blank=False)
    body = models.TextField(null=False, blank=False)
    publish = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.profile} - {self.name}"


class GuidePersonalTour(models.Model):
    class Meta:
        verbose_name_plural = "Персональні екскурсії"

    profile = models.ForeignKey(GuideProfile, on_delete=models.CASCADE, null=False, blank=False)
    title = models.TextField(null=False, blank=False)
    body = models.TextField(null=False, blank=False)
    duration = models.FloatField(null=False, blank=False)
    price = models.FloatField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.profile} - {self.title}"
