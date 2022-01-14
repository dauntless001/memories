from django.db import models 

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