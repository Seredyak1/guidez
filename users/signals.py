from django.dispatch import receiver
from django.db.models.signals import post_save

from django.contrib.auth.models import User


@receiver(post_save, sender=User)
def create_blog_for_new_user(sender, created, instance, **kwargs):
    """Signal to create personal blog for new User"""
    if created:
        Blog.objects.create(user=instance)
