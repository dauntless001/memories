from django.db import models 
from django.utils.crypto import get_random_string
import random

class TimeBasedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ['-created_at']

class UserBasedModel(models.Model):
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
    
    class Meta:
        abstract = True


def gen_slug():
    return get_random_string(length=random.randint(8, 11))