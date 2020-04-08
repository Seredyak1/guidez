from django.db import models

from django.contrib.auth import get_user_model
User = get_user_model()


class GuidePersonalTour(models.Model):
    class Meta:
        verbose_name_plural = "Персональні екскурсії"

    user = models.ForeignKey(User,  related_name="user_personal_tour",
                             on_delete=models.CASCADE, null=False, blank=False)
    title = models.TextField(null=False, blank=False)
    body = models.TextField(null=False, blank=False)
    place = models.TextField(blank=True, null=True)
    duration = models.FloatField(null=False, blank=False)
    price = models.FloatField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user} - {self.title}"
