from django.db import models


class EmailTemplate(models.Model):
    class Meta:
        verbose_name = "Шаблон імейлу"
        verbose_name_plural = "Шаблони імейлів"

    title = models.CharField(max_length=256, null=True, blank=True)
    body = models.TextField(null=True, blank=True)
    type = models.CharField(max_length=256, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title or "EmailTemplate"
