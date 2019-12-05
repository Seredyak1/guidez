import uuid
from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin

from email_service.email_service import confirm_email


class MyUserManager(BaseUserManager):
    """Manager for custom User"""
    def _create_user(self, email, password=None, **extra_fields):
        """Creates and saves a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        if not password:
            raise ValueError('The given password must be set')
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        user.send_confirm_email()
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_active', True)

        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_admin', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):

    class Meta:
        verbose_name = 'Користувач'
        verbose_name_plural = 'Користувачі'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True, blank=False, null=False)
    first_name = models.CharField(max_length=128, blank=True, null=True)
    last_name = models.CharField(max_length=128, blank=True, null=True)

    date_of_birth = models.DateField(blank=True, null=True)
    phone = models.TextField(blank=True, null=True)
    city = models.TextField(blank=True, null=True)
    personal_description = models.TextField(null=True, blank=True)
    language = ArrayField(models.TextField(blank=True, null=True),
                            size=16, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    validation_image = models.ImageField(upload_to='profile_validation/', null=True, blank=True)
    profile_image = models.ImageField(upload_to=f'{str(id)}/', null=True, blank=True)

    is_valid = models.BooleanField(default=False)
    is_active = models.BooleanField('is_active', default=False)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField('staff status', default=False)
    is_superuser = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    objects = MyUserManager()

    def __str__(self):
        return self.email

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def send_confirm_email(self):
        """Send confirm email about success registration"""
        confirm_email(self.email, self.get_full_name())
