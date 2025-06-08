from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from cloudinary.models import CloudinaryField
from django.dispatch import receiver


class CustomUser(AbstractUser):
    """
    Custom user model that extends the default Django user model.
    This allows for additional fields and customization in the future.
    """
    email = models.EmailField(unique=True, blank=False, null=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
        ordering = ['-date_joined']
    
    def __str__(self):
        return self.email
    
class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    profile_picture = CloudinaryField('image', blank=True, null=True, default='default_profile_qtk8ec')
    
    def __str__(self):
        return f"{self.user.email}'s profile"

@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    """
    Signal to create a Profile when a new CustomUser is created.
    """
    if created:
        Profile.objects.create(user=instance)
        
post_save.connect(create_user_profile, sender=CustomUser)