from django.db import models

from django.contrib.auth import get_user_model
User = get_user_model()


class Blog(models.Model):

    class Meta:
        verbose_name = "Обговорення"
        verbose_name_plural = "Обговорення"
        ordering = ("-created_at",)

    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False)
    title = models.TextField(blank=False, null=False)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Comment(models.Model):

    class Meta:
        verbose_name = "Коментар"
        verbose_name_plural = "Коментарі"
        ordering = ("-created_at",)

    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, blank=False, null=False)
    body = models.TextField(blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.get_full_name()} to {self.blog.title}"
