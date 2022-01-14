from rest_framework.authtoken.models import Token
from accounts.models import User, Profile
from django.db.models.signals import post_save

def save_profile(sender, instance, created, **kwargs):
    if created:
        Token.objects.create(user=instance)
        Profile.objects.create(user=instance)

post_save.connect(save_profile, sender=User)
