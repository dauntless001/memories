from django.db import models
from django.contrib.auth.models import AbstractUser
from memories.utils import image_utils
from django.conf import settings
# Create your models here.

class User(AbstractUser):
    pass

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    display_name = models.CharField(max_length=255, default='Something great about me')
    image = models.ImageField(null=True, blank=True, 
        upload_to=image_utils.get_upload_path)


    def __str__(self):
        return f'{self.user.username} profile'
    
    def image_url(self):
        if self.image:
            return getattr(self.image, 'url', None)
        return f'{settings.STATIC_URL}images/avatar-2.jpg'