from django.db import models
from memories.utils import model_utils
# Create your models here.


class Post(model_utils.TimeBasedModel, model_utils.UserBasedModel):
    caption = models.TextField()
    slug = models.SlugField(default=model_utils.gen_slug)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.user.username} - memories {self.slug}'
    
