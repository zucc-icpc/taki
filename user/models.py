from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from user.storage import OverwriteStorage
TYPE_CHOICES = sorted((item, item) for item in ('普通用户', '队员', '教练', '退役队员'))


class Profile(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE, primary_key=True, related_name='profile')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)
    type = models.CharField(choices=TYPE_CHOICES, max_length=10, blank=False, default='普通用户')
    biography = models.CharField(max_length=5000, blank=True, default='')
    avatar = models.ImageField(upload_to='avatar', storage=OverwriteStorage(), max_length=100)
    name = models.CharField(max_length=10, blank=True, default='')
    sid = models.CharField(max_length=10, blank=True, default='')
    level = models.CharField(max_length=10, blank=True, default='')

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    class Meta:
        ordering = ('created_at',)
        db_table = "auth_profile"