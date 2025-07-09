import secrets
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import timedelta
from django.utils import timezone


class EmailVerificationToken(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='verification_tokens')
    token = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField()
    used = models.BooleanField(default=False)
    used_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'email_verification_tokens'
    

    def save(self, *args, **kwargs):
        if not self.token:
            self.token = secrets.token_urlsafe(32)
        if not self.expires_at:
            self.expires_at = timezone.now() + timedelta(hours=24)

        super().save(*args, **kwargs)

    def is_expired(self):
        return timezone.now() > self.expires_at
    
    def is_valid(self):
        return not self.used and not self.is_expired()

    def mark_as_used(self):
        self.used = True
        self.used_at = timezone.now()
        self.save()

    def __str__(self):
        return f"Token para {self.user.username}"


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(max_length=700, blank=True)
    phone = models.CharField(max_length=15, blank=True)
    avatar = models.TextField(blank=True)
    birth_date = models.DateField(null=True, blank=True)
    email_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "user_profiles"

    def __str__(self):
        return f"{self.user.username}"



class UserActivity(models.Model):
    ACTION_CHOICES = [
        ('LOGIN', 'Inicio de sesión'),
        ('LOGOUT', 'Cierre de sesión'),
        ('PASSWORD_CHANGE', 'Cambio de contraseña'),
        ('PROFILE_UPDATE', 'Actualización de perfil'),
        ('FAILED_LOGIN', 'Intento de inicio de sesión fallido')
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='activities')
    action = models.CharField(max_length=100, choices=ACTION_CHOICES)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    user_agent = models.TextField(blank=True)
    details = models.JSONField(blank=True, default=dict)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        db_table = "user_activities"
        verbose_name = "Actividad del usuario"
        verbose_name_plural = "Actividades de los usuarios"

    def __str__(self):
        return f"{self.user.username} - {self.action}"


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """create profile after user created"""
    print(sender)
    if created:
        UserProfile.objects.create(user=instance)


