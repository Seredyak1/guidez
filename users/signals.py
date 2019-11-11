from django.dispatch import receiver
from django.db.models.signals import post_save

from django.contrib.auth.models import User
from guide_profile.models import GuideProfile

@receiver(post_save, sender=User)
def create_blog_for_new_user(sender, created, instance, **kwargs):
    """Signal to create personal blog for new User"""
    if created:
        profile = GuideProfile.objects.create(auth_user=instance)
        user = User
        profile.first_name = user.first_name
        profile.last_name = user.last_name
        profile.email = user.email
        profile.save()
