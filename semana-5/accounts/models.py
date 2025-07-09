from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(max_length=700, blank=True)
    phone = models.CharField(max_length=15, blank=True)
    avatar = models.TextField(blank=True)
    birth_date = models.DateField(null=True, blank=True)
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


